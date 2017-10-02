import numpy as np
from pynwb import get_class, load_namespaces
from datetime import datetime
from pynwb import NWBFile
from form.backends.hdf5 import HDF5IO
from pynwb import get_build_manager


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

test_file_name = 'example.nwb'

manager = get_build_manager()
io = HDF5IO(test_file_name, manager, mode='w')
io.write(f)
io.close()


io = HDF5IO(test_file_name, mode='r')
read_data = io.read()
pst = read_data.get_raw_timeseries('my_population')
print pst.data[2:5]
print pst.timestamps[2:5]