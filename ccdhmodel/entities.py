# Auto generated from entities.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-19 08:23
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
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import Uriorcurie

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
class EntityId(URIorCURIE):
    pass


class OrganizationId(EntityId):
    pass


class DocumentReferenceId(EntityId):
    pass


class ConditionDiagnosisId(EntityId):
    pass


class VisitId(EntityId):
    pass


class ProjectId(EntityId):
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



# Slots
class slots:
    pass

slots.id = Slot(uri=CCDH.id, name="id", curie=CCDH.curie('id'),
                      model_uri=CCDH.id, domain=None, range=URIRef)

slots.Entity_id = Slot(uri=CCDH.id, name="Entity_id", curie=CCDH.curie('id'),
                      model_uri=CCDH.Entity_id, domain=Entity, range=Union[str, EntityId])
