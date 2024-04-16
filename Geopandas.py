import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("./data/local_level.shp")
gdf.to_crs(epsg = 4326)
crs= gdf.crs;
print(gdf)
gdf.to_file("./data/local_level.geojson",driver = "GeoJSON") # to create a file into another format

# to get the boundaries of the given data
gdf["boundary"] = gdf.boundary;
print(gdf["boundary"])

# to get the centroids
gdf["centroid"] =  gdf.centroid;
print(gdf["centroid"])

# to get the distance from the centroid of the first place in file
first_point = gdf["centroid"].iloc[0]
gdf["distance"] = gdf["centroid"].distance(first_point)
print(gdf["distance"])
print(gdf["distance"].mean)

gdf.plot("DISTRICT",legend=False)
plt.show()

print(gdf.crs)