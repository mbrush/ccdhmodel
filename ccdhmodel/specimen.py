# Auto generated from specimen.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-19 08:23
# Schema: specimen
#
# id: https://ccdh.org/model/specimen
# description: Any material sample taken from a biological entity (living or dead), or taken from a physical
#              object or the environment. (Adapted from FHIR) Specimens are usually collected as an example of
#              their kind, often for use in some investigation.
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
from datatypes import Literal
from entities import Entity
from includes.types import String, Uriorcurie

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ADM = CurieNamespace('ADM', 'https://ccdh.org/models/ADM/')
GDC = CurieNamespace('GDC', 'http://fill.me.in/GDC')
HTAN = CurieNamespace('HTAN', 'http://fill.me.in/HTAN')
ICDC = CurieNamespace('ICDC', 'http://fill.me.in/ICDC')
PDC = CurieNamespace('PDC', 'http://fill.me.in/PDC')
SPECIMEN = CurieNamespace('specimen', 'https://ccdh.org/specimen/')
DEFAULT_ = SPECIMEN


# Types

# Class references



@dataclass
class Specimen(YAMLRoot):
    """
    -> Any material sample taken from a biological entity (living or dead), or taken from a physical object or the
    environment. (Adapted from FHIR) Specimens are usually collected as an example of their kind, often for use in
    some investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPECIMEN.Specimen
    class_class_curie: ClassVar[str] = "specimen:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = SPECIMEN.Specimen

    id: Optional[Union[str, Literal]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, Literal):
            self.id = Literal(self.id)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=SPECIMEN.id, name="id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.id, domain=None, range=Optional[Union[str, Literal]], mappings = [ADM["Sample.sample_id"], ADM["Portion.portion_id"], ADM["Aliquot.aliquot_id"], ADM["Analyte.analyte_id"], GDC["Aliquot.id"], GDC["Analyte.id"], GDC["Portion.id"], GDC["Sample.id"], PDC["Aliquot.aliquot_id"], PDC["Analyte.analyte_id"], PDC["Portion.portion_id"], PDC["Sample.sample_id"], ICDC["Sample.sample_id"], HTAN["Biospecimen.HTAN_BIOSPECIMEN_ID"]])

slots.Specimen_id = Slot(uri=SPECIMEN.id, name="Specimen_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Specimen_id, domain=Specimen, range=Optional[Union[str, Literal]])

slots.Entity_id = Slot(uri=SPECIMEN.id, name="Entity_id", curie=SPECIMEN.curie('id'),
                      model_uri=SPECIMEN.Entity_id, domain=Entity, range=Union[str, EntityId])
