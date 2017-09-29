from pynwb import NWBNamespaceBuilder, NWBGroupSpec, NWBDatasetSpec
import numpy as np
from pynwb import get_class, load_namespaces
from datetime import datetime
from pynwb import NWBFile
from form.backends.hdf5 import HDF5IO
from pynwb import get_build_manager


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

ns_path = "alleninstitute.namespace.yaml"
load_namespaces(ns_path)

PopulationSpikeTrain = get_class('PopulationSpikeTrain', 'alleninstitute')
fs = PopulationSpikeTrain(data=(10*np.random.random(5)).astype(np.int),
                          name='my_population',
                          source='acquisition',
                          unit='second',
                          timestamps=np.random.rand(5))

f = NWBFile(source='noone',
            session_description='my first synthetic recording',
            file_name='tmp.nwb',
            identifier='hi',
            experimenter='Dr. Bilbo Baggins',
            lab='Bag End Labatory',
            institution='University of Middle Earth at the Shire',
            experiment_description='empty',
            session_id='LONELYMTN',
            session_start_time=datetime.now())

f.add_raw_timeseries(fs)

manager = get_build_manager()
io = HDF5IO('tmp.nwb', manager, mode='w')
io.write(f)
io.close()
