from owlready2 import *

onto = get_ontology("http://example.org/conceptual_spaces.owl")

with onto:
    # === Classes ===
    class ConceptualSpace(Thing): pass
    class Context(Thing): pass
    class Domain(Thing): pass
    class Concept(Thing): pass
    class Instance(Thing): pass
    class ContrastClass(Thing): pass
    class Property(Concept): pass
    class QualityDimension(Thing): pass
    class ConvexRegion(Thing): pass
    class PrototypicalInstance(Instance): pass
    class MeasurementSystem(Thing): pass
    

    # === Object Properties ===
    class has_context(ConceptualSpace >> Context): pass
    class has_domain(ConceptualSpace >> Domain): pass
    class has_concept(ConceptualSpace >> Concept): pass
    class has_instance(ConceptualSpace >> Instance): pass
    class has_contrast_class(ConceptualSpace >> ContrastClass): pass
    class has_quality_dimension(Domain >> QualityDimension): pass
    class has_region(Concept >> ConvexRegion): pass
    class has_prototypical_instance(Concept >> PrototypicalInstance): pass
    class corresponds_to(ConvexRegion >> Domain): pass
    class uses_measurement_system(QualityDimension >> MeasurementSystem): pass

    # === Data Properties ===
    class has_similarity_parameter(ConceptualSpace >> int, DataProperty): pass
    class has_measurement_level(QualityDimension >> str, DataProperty): pass
    class has_min_range(QualityDimension >> float, DataProperty): pass
    class has_max_range(QualityDimension >> float, DataProperty): pass
    class is_circular(QualityDimension >> bool, DataProperty): pass

    # === Individuals ===
    commonsense_cs = ConceptualSpace('CommonSense_ConceptualSpace')

    weight_domain = Domain('Weight_Domain')
    weight_dimension = QualityDimension('Weight')
    kg_measurement = MeasurementSystem('MetricKG')

    color_domain_rgb = Domain('Color_RGB')
    color_red_dimension = QualityDimension('Red_Value')
    color_green_dimension = QualityDimension('Green_Value')
    color_blue_dimension = QualityDimension('Blue_Value')

    orange_fruit_concept = Concept('Orange_Fruit')
    orange_fruit_proto = PrototypicalInstance('MostOrangeOrangeFruit')
    
    orange_color_concept = Concept('Orange_Color')
    orange_color_proto = PrototypicalInstance('MostOrangeOrangeColor')

    # === Assign Class Attributes ===
    commonsense_cs.has_concept = [orange_fruit_concept, orange_color_concept]
    commonsense_cs.has_domain = [color_domain_rgb, weight_domain]
    commonsense_cs.has_instance = [orange_fruit_proto, orange_color_proto]

    weight_domain.has_quality_dimension = [weight_dimension]
    weight_dimension.has_min_range = [0]
    weight_dimension.has_max_range = [999]
    weight_dimension.is_circular = [False]
    weight_dimension.has_measurement_level = ['interval']
    weight_dimension.uses_measurement_system = [kg_measurement]

    color_domain_rgb.has_quality_dimension = [color_red_dimension, color_green_dimension, color_blue_dimension]
    color_red_dimension.has_min_range = [0]
    color_red_dimension.has_max_range = [255]
    color_red_dimension.is_circular = [False]
    color_red_dimension.has_measurement_level = ['interval']
    color_green_dimension.has_min_range = [0]
    color_green_dimension.has_max_range = [255]
    color_green_dimension.is_circular = [False]
    color_green_dimension.has_measurement_level = ['interval']
    color_blue_dimension.has_min_range = [0]
    color_blue_dimension.has_max_range = [255]
    color_blue_dimension.is_circular = [False]
    color_blue_dimension.has_measurement_level = ['interval']

    # orange_fruit_concept.has_prototypical_instance = [orange_fruit_proto]

    # orange_color_concept.has_prototypical_instance = [orange_color_proto]

def extend_property_dimension(onto):
    """
    Extends the ontology with a data property for each quality dimension.
    """
    pass

def print_ontology_summary(onto):
    print("=== Classes ===")
    for cls in onto.classes():
        print(f"- {cls.name}")

    print("\n=== Object Properties ===")
    for prop in onto.object_properties():
        print(f"- {prop.name}")
        print(f"  Domain: {prop.domain}")
        print(f"  Range: {prop.range}")

    print("\n=== Data Properties ===")
    for prop in onto.data_properties():
        print(f"- {prop.name}")
        print(f"  Domain: {prop.domain}")
        print(f"  Range: {prop.range}")

    print("\n=== Individuals ===")
    for indiv in onto.individuals():
        print(f"- {indiv.name}: {indiv.is_a}")

    print("\n=== Assertions ===")
    for indiv in onto.individuals():
        print(f"\nIndividual: {indiv.name}")
        for prop in indiv.get_properties():
            for value in prop[indiv]:
                print(f"  {prop.name} -> {value}")


# Optional: Save it for future disappointment
onto.save(file="cs4cs.owl", format="rdfxml")
print_ontology_summary(onto)