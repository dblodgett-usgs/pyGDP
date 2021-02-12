from lettuce import *
from nose.tools import assert_equal


@step(r'Given I want to access shapefiles on some bogus server')
def point_to_bogus_geoserver(step):
    import pyGDP
    test_pyGDP = pyGDP.pyGDPwebProcessing(wfs_url='https://bogus/bogy/geoserver/wfs')
    world.bogus_wfs = test_pyGDP.wfsUrl


@step(r'Then I want to make sure that bogus server is actually getting set')
def point_to_bogus_geoserver_test(step):
    assert_equal(world.bogus_wfs, 'https://bogus/bogy/geoserver/wfs')
