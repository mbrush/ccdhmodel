# Auto generated from entities.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-24 13:36
# Schema: entities
#
# id: https://ccdh.org/model/entities
# description: This sheet holds descriptions of objects referenced as the Data Type of a field in the Biospecimen
#              CDM, and likely to be represented as Entities/Classes/Resources in our final model, but which are
#              out of scope to fully define in the current phase of work. We will record these candidate
#              Entities/Classes/Resources here, and document their proposed use and requirements to support
#              Biospecimen representation. Requiremetns accrued as we model additional subdomains will inform if
#              and how these entties are represented in our model.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from datatypes import Literal
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BRIDG = CurieNamespace('BRIDG', 'https://fill.me.in/BRIDG/')
FHIR = CurieNamespace('FHIR', 'http://hl7.org/fhir/')
CCDH = CurieNamespace('ccdh', 'https://ccdh.org/')
DEFAULT_ = CCDH


# Types

# Class references
class EntityId(Literal):
    pass


class OrganizationId(Literal):
    pass


class DocumentReferenceId(Literal):
    pass


class ConditionDiagnosisId(Literal):
    pass


class VisitId(Literal):
    pass


class ProjectId(Literal):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Entity
    class_class_curie: ClassVar[str] = "ccdh:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CCDH.Entity

    id: Union[str, EntityId]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Organization(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Organization
    class_class_curie: ClassVar[str] = "ccdh:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = CCDH.Organization

    id: Union[str, OrganizationId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class DocumentReference(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.DocumentReference
    class_class_curie: ClassVar[str] = "ccdh:DocumentReference"
    class_name: ClassVar[str] = "DocumentReference"
    class_model_uri: ClassVar[URIRef] = CCDH.DocumentReference

    id: Union[str, DocumentReferenceId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DocumentReferenceId):
            self.id = DocumentReferenceId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class ConditionDiagnosis(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.ConditionDiagnosis
    class_class_curie: ClassVar[str] = "ccdh:ConditionDiagnosis"
    class_name: ClassVar[str] = "ConditionDiagnosis"
    class_model_uri: ClassVar[URIRef] = CCDH.ConditionDiagnosis

    id: Union[str, ConditionDiagnosisId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ConditionDiagnosisId):
            self.id = ConditionDiagnosisId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Visit(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Visit
    class_class_curie: ClassVar[str] = "ccdh:Visit"
    class_name: ClassVar[str] = "Visit"
    class_model_uri: ClassVar[URIRef] = CCDH.Visit

    id: Union[str, VisitId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, VisitId):
            self.id = VisitId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Project(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Project
    class_class_curie: ClassVar[str] = "ccdh:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = CCDH.Project

    id: Union[str, ProjectId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)
        super().__post_init__(**kwargs)


class PatientOrBiologicallyDerivedMaterial(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.PatientOrBiologicallyDerivedMaterial
    class_class_curie: ClassVar[str] = "ccdh:PatientOrBiologicallyDerivedMaterial"
    class_name: ClassVar[str] = "PatientOrBiologicallyDerivedMaterial"
    class_model_uri: ClassVar[URIRef] = CCDH.PatientOrBiologicallyDerivedMaterial


class Patient(PatientOrBiologicallyDerivedMaterial):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Patient
    class_class_curie: ClassVar[str] = "ccdh:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = CCDH.Patient


class BiologicallyDerivedMaterial(PatientOrBiologicallyDerivedMaterial):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedMaterial
    class_class_curie: ClassVar[str] = "ccdh:BiologicallyDerivedMaterial"
    class_name: ClassVar[str] = "BiologicallyDerivedMaterial"
    class_model_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedMaterial


class BiologicallyDerivedProduct(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedProduct
    class_class_curie: ClassVar[str] = "ccdh:BiologicallyDerivedProduct"
    class_name: ClassVar[str] = "BiologicallyDerivedProduct"
    class_model_uri: ClassVar[URIRef] = CCDH.BiologicallyDerivedProduct


class SpecimenCreationActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenCreationActivity"
    class_name: ClassVar[str] = "SpecimenCreationActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenCreationActivity


class SpecimenProcessingActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenProcessingActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenProcessingActivity"
    class_name: ClassVar[str] = "SpecimenProcessingActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenProcessingActivity


class SpecimenStorageActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenStorageActivity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenStorageActivity"
    class_name: ClassVar[str] = "SpecimenStorageActivity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenStorageActivity


class SpecimenTransportActvity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenTransportActvity
    class_class_curie: ClassVar[str] = "ccdh:SpecimenTransportActvity"
    class_name: ClassVar[str] = "SpecimenTransportActvity"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenTransportActvity


class DataContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.DataContainer
    class_class_curie: ClassVar[str] = "ccdh:DataContainer"
    class_name: ClassVar[str] = "DataContainer"
    class_model_uri: ClassVar[URIRef] = CCDH.DataContainer


class SpecimenContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.SpecimenContainer
    class_class_curie: ClassVar[str] = "ccdh:SpecimenContainer"
    class_name: ClassVar[str] = "SpecimenContainer"
    class_model_uri: ClassVar[URIRef] = CCDH.SpecimenContainer


class Relationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.Relationship
    class_class_curie: ClassVar[str] = "ccdh:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = CCDH.Relationship


class BodyStructure(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCDH.BodyStructure
    class_class_curie: ClassVar[str] = "ccdh:BodyStructure"
    class_name: ClassVar[str] = "BodyStructure"
    class_model_uri: ClassVar[URIRef] = CCDH.BodyStructure



# Slots
class slots:
    pass

slots.id = Slot(uri=CCDH.id, name="id", curie=CCDH.curie('id'),
                      model_uri=CCDH.id, domain=None, range=URIRef)
