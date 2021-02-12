import pyGDP

pyGDP = pyGDP.pyGDPwebProcessing()

shapefile = 'sample:CONUS_states'
attribute = 'STATE'
value = 'Alabama'

dataSetURI = 'https://cida.usgs.gov/ArcGIS/services/SSURGO_Products/MapServer/WCSServer'

dataType = '1'

pyGDP.submitFeatureCoverageWCSIntersection(shapefile, dataSetURI, dataType, attribute, value, verbose=True)
