from pynwb import NWBNamespaceBuilder, NWBGroupSpec, NWBDatasetSpec

ns_path = "alleninstitute.namespace.yaml"
ext_source = "alleninstitute.extensions.yaml"
nwb_ds = NWBDatasetSpec('dataset_doc', 'int', 'data')

ns_builder = NWBNamespaceBuilder('Allen Institute extensions', "alleninstitute")
ext = NWBGroupSpec('A custom TimeSeries that stores neuron gids and times',
                   datasets=[nwb_ds],
                   neurodata_type_inc='TimeSeries',
                   neurodata_type_def='PopulationSpikeTrain')

ns_builder.add_spec(ext_source, ext)
ns_builder.export(ns_path)