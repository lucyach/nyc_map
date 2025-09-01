import folium

# Center of NYC
nyc_center = [40.72965, -73.98651]

# List of locations to mark: (name, latitude, longitude)
locations = [
    ("LUCYS HOUSE", 40.72965, -73.98651, "home"),
    ("Ground Zero 9/11 Memorial & Museum", 40.71194409423603, -74.01348897367062, "museum"),
    ("Brooklyn Flea Market", 40.702588, -73.987735, "store"),
    ("The High Line", 40.7481, -74.0047, "activity"),
    ("Pepe Giallo (Italian restaurant on High Line)", 40.7442, -74.0049, "restaurant"),
    ("Metropolitan Museum of Art", 40.7795909308426, -73.96326546096661, "museum"),
    ("MoMA (Museum of Modern Art)", 40.76325298705367, -73.96972517934122, "museum"),
    ("MOMA PS1 (Contemporary Art)", 40.74594278889299, -73.94716137318795, "museum"),
    ("Big Reuse Store", 40.67225458321197, -73.99672498478911, "store"),
    ("Search and Destroy Store", 40.729219433689806, -73.98852937309945, "store"),
    ("L Train Vintage / Urban Jungle", 40.705241364791455, -73.92956511188738, "store"),
    ("Chinatown, Manhattan", 40.71819596948126, -73.99252499283197, "activity"),
    ("Boxers NYC (Washington Heights)", 40.74128506125525, -73.99325883076948, "club/bar"),
    ("Market Hotel (Bushwick)", 40.69708958246249, -73.93462881545213, "club/bar"),
    ("American Museum of Natural History", 40.78149470294837, -73.9740203866429, "museum"),
    ("Time Out Market (DUMBO area)", 40.70358316942507, -73.99214570007038, "restaurant"),
    ("Oyishi Sushi (near MET)", 40.77540400265574, -73.95544597256219, "restaurant"),
    ("Lower East Side for DJs", 40.71847031817319, -73.98782878404761, "club/bar"),
    ("Elsewhere Club (Brooklyn)", 40.709770289078676, -73.92323097988586, "club/bar"),
    ("Alphabet City Neighborhood", 40.72589660860112, -73.97934794707074, "activity"),
    ("Lovers of Today Bar", 40.7259961454154, -73.98345378662009, "club/bar"),
    ("Staten Island Ferry", 40.70150400823482, -74.0133962307327, "activity"),
    ("The Strand Bookstore", 40.735510519379105, -73.99127337215997, "store"),
    ("Fushimi Market", 40.74690639442177, -73.98977995779416, "store"),
    ("Central Park", 40.78268468080871, -73.96564777314906, "park"),
    ("Stonewall Inn", 40.73405210332597, -74.00214114245857, "club/bar"),
    ("National Museum of the American Indian", 40.70410810105897, -74.0136889000878, "museum"),
    ("Whitney Museum of American Art", 40.73975841010002, -74.00890581544209, "museum"),
    ("Washington Square Park", 40.73112770333569, -73.99737491548636, "park"),
    ("McDougal Street", 40.73011236509266, -74.00062910194019, "activity"),
    ("Tompkins Square Park", 40.726803509793726, -73.98171972714188, "park"),
    ("Fort Greene Park", 40.6918389459963, -73.97511725421661, "park"),
    ("National Jazz Museum in Harlem", 40.8102632403638, -73.9429838118673, "museum"),
    ("Trinity Churchyard", 40.83318065248414, -73.94917304427814, "other"),
    ("Seaglass Carousel at Battery Park", 40.702340273361685, -74.01503408659397, "activity"),
    ("Brooklyn Botanical Garden", 40.66905178690165, -73.96449105786516, "activity"),
    ("Museum of the Moving Image", 40.75662171792481, -73.92397105785173, "museum"),
    ("Noguchi Museum", 40.76712177720009, -73.93813973084133, "museum"),
    ("Fort Tilden Beach", 40.55995617267501, -73.88764728663617, "park"),
    ("Bossa Nova Civic Club", 40.698236728746764, -73.92792190015818, "club/bar"),
    ("Nowadays Bushwick Club", 40.692624596179975, -73.90149288478176, "club/bar"),
    ("Brooklyn Steel Venue", 40.719422752244256, -73.93870806942547, "venue"),
    ("Brooklyn Monarch Venue", 40.71100688614372, -73.9361860424009, "venue"),
    ("Trans Pecos Club", 40.697391369495776, -73.90609366945495, "club/bar"),
    ("Bushwick Collective (Graffiti Art Gallery)", 40.70763939460192, -73.92221668660602, "other"),
    ("Tannen's Magic Shop", 40.749863145031405, -73.98693502896411, "store"),
    ("Central Park Boat Rental", 40.775271421051, -73.968752957798, "activity"),
    ("Little Island Park", 40.742148717647076, -74.01036337310617, "park"),
    ("Little Italy", 40.71950524834782, -73.99723215806527, "activity"),
    ("NYU (New York University)", 40.73453345870364, -73.9938532958971, "other"),
    ("TV Eye (Punk Venue)", 40.698008948869024, -73.90527214427885, "venue"),
    ("McGee's Pub", 40.76503502313631, -73.98296081358961, "club/bar"),
    ("House of Yes", 40.70706222200007, -73.92358822649253, "club/bar"),
    ("Don't Tell Mama Piano Bar", 40.76074545024818, -73.98951822893927, "club/bar"),
    ("Pier 17 (Rooftop Concert)", 40.705608698004475, -74.00166425778005, "venue"),
    ("Bedford Ave (Brooklyn)", 40.65396483008125, -73.95621201542403, "activity"),
    ("Carrie Bradshaw's Apartment (66 Perry St)", 40.73553929134069, -74.0039028154642, "other"),
    ("Daredevil Tattoo Museum", 40.714639370934364, -73.99094211546488, "museum"),
    ("George Glazer Gallery", 40.78271580457388, -73.94736482705805, "museum"),
    ("White Horse Tavern", 40.740640275674906, -74.00619200437554, "club/bar"),
    ("Mercury Lounge", 40.72228143658013, -73.986778086596, "venue"),
    ("Shakespeare in Central Park", 40.78070088555576, -73.96891357523388, "activity"),
    ("Prospect Park Carousel", 40.66394291947269, -73.96429124427955, "activity"),
    ("Summit One Vanderbilt", 40.75296965853865, -73.97866092708148, "activity"),
    ("Broadway (Hamilton or Cursed Child)", 40.76338654475623, -73.98307432707146, "venue"),
    ("Hamilton Grange National Memorial", 40.82148228580702, -73.9472809424264, "museum"),
    ("Museum of Reclaimed Urban Space", 40.72599376064957, -73.9779247425263, "museum"),
    ("Rubulad", 40.70467429999638, -73.92732352525321, "club/bar"),
    ("Bronx Zoo", 40.850247001894914, -73.8767109712605, "activity"),
    ("Summer on the Hudson (West Side County Fair)", 40.8000, -73.9600, "activity"),
    ("Ferragosto Italian Culture Celebration", 40.8000, -73.9600, "activity"),
    ("Nonna's of the World", 40.64217707346529, -74.07723494057129, "restaurant")
]




# Create the map
m = folium.Map(location=nyc_center, zoom_start=11)

# --- CLUSTERING AND CIRCLES ---
from sklearn.cluster import DBSCAN
import numpy as np

# Prepare coordinates for clustering
coords = np.array([(lat, lon) for _, lat, lon, _ in locations])

 # DBSCAN clustering (eps in degrees, min_samples=2 for a clump)
 # eps=0.004 ~ 400m, slightly larger walkable area
db = DBSCAN(eps=0.004, min_samples=2).fit(coords)
labels = db.labels_


# --- Find clusters and merge overlapping circles ---
cluster_info = []
unique_labels = set(labels)
for label in unique_labels:
    if label == -1:
        continue  # noise
    cluster_points = coords[labels == label]
    if len(cluster_points) >= 2:
        center = cluster_points.mean(axis=0)
        dists = np.linalg.norm(cluster_points - center, axis=1)
        radius = dists.max() * 111000 + 100  # meters (1 deg ~ 111km), add small padding
        cluster_info.append({'center': center, 'points': cluster_points, 'radius': radius})

# Merge clusters if their circles overlap
def circles_overlap(c1, r1, c2, r2):
    dist = np.linalg.norm(c1 - c2) * 111000
    return dist < (r1 + r2)

merged = [False] * len(cluster_info)
final_clusters = []
for i, ci in enumerate(cluster_info):
    if merged[i]:
        continue
    # Find all clusters overlapping with i
    group = [i]
    for j in range(i+1, len(cluster_info)):
        if not merged[j] and circles_overlap(ci['center'], ci['radius'], cluster_info[j]['center'], cluster_info[j]['radius']):
            group.append(j)
            merged[j] = True
    # Merge all points in group
    all_points = np.vstack([cluster_info[k]['points'] for k in group])
    center = all_points.mean(axis=0)
    dists = np.linalg.norm(all_points - center, axis=1)
    radius = dists.max() * 111000 + 100
    final_clusters.append({'center': center, 'radius': radius})

# Draw merged circles only if they contain at least two markers
for c in final_clusters:
    # Count how many points are in the cluster (radius)
    # If radius is zero, it means only one marker
    if c['radius'] > 0:
        folium.Circle(
            location=c['center'],
            radius=c['radius'],
            color='gray',
            fill=True,
            fill_opacity=0.4,
            weight=4
        ).add_to(m)

# Add markers for each location

# Extended color gradient for markers
colors = [
    'red',
    'orange',
    'green',
    'blue',
    'purple',
    'pink',
    'gray',
]


# Icon mapping for each type
icon_map = {
    'museum': 'book',
    'store': 'shopping-cart',
    'activity': 'star',
    'restaurant': 'cutlery',
    'club/bar': 'glass',
    'venue': 'music',
    'other': 'info-sign',
    'home': 'home',
    'park': 'tree-conifer'
}

for idx, (name, lat, lon, loc_type) in enumerate(locations):
        color_idx = (idx - 1) // 12
        color = colors[color_idx] if color_idx < len(colors) else 'gray'
        icon_symbol = icon_map.get(loc_type, 'info-sign')
        folium.Marker(
            [lat, lon],
            popup=name,
            icon=folium.Icon(color=color, icon=icon_symbol)
        ).add_to(m)

# Save to HTML file
m.save("index.html")
print("Map saved as index.html")