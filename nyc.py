import folium

# Center of NYC
nyc_center = [40.72965, -73.98651]

# List of locations to mark: (name, latitude, longitude)
locations = [
    ("LUCYS HOUSE", 40.72965, -73.98651, "home", "yayyyyy"),
    ("Ground Zero 9/11 Memorial & Museum", 40.71194409423603, -74.01348897367062, "museum", "Memorial open 24/7; museum free Mondays 5:30-7 with day-of reservation"),
    ("Brooklyn Flea Market", 40.702588, -73.987735, "store", "Weekend flea market every Saturday and Sunday"),
    ("The High Line", 40.7481, -74.0047, "activity", "Elevated park walk; free"),
    ("Pepe Giallo (Italian restaurant on High Line)", 40.7442, -74.0049, "restaurant", "Italian restaurant recommended by Tejan"),
    ("Metropolitan Museum of Art", 40.7795909308426, -73.96326546096661, "museum", "Major art museum; recommended by Tejan and Wally"),
    ("MoMA (Museum of Modern Art)", 40.76325298705367, -73.96972517934122, "museum", "Modern art museum; combine with MOMA PS1 ticket; Tejan rec"),
    ("MOMA PS1 (Contemporary Art)", 40.74594278889299, -73.94716137318795, "museum", "Contemporary art; combine with MoMA ticket; Tejan rec"),
    ("Big Reuse Store", 40.67225458321197, -73.99672498478911, "store", "Reuse and salvage store; like Urban Ore; Wally rec"),
    ("Search and Destroy Store", 40.729219433689806, -73.98852937309945, "store", "Punk clothing store; Wally rec"),
    ("L Train Vintage / Urban Jungle", 40.705241364791455, -73.92956511188738, "store", "Huge thrift store; Lucy rec"),
    ("Chinatown, Manhattan", 40.71819596948126, -73.99252499283197, "activity", "Budget-friendly neighborhood, cash only; Lucy rec"),
    ("Boxers NYC (Washington Heights)", 40.74128506125525, -73.99325883076948, "club/bar", "Gay club; J rec"),
    ("Market Hotel (Bushwick)", 40.69708958246249, -73.93462881545213, "club/bar", "DJ venue in Bushwick; Tejan rec"),
    ("American Museum of Natural History", 40.78149470294837, -73.9740203866429, "museum", "$24 with student ID; Tejan rec"),
    ("Time Out Market (DUMBO area)", 40.70358316942507, -73.99214570007038, "restaurant", "Breakfast or meals after biking Brooklyn Bridge; Tejan rec"),
    ("Oyishi Sushi (near MET)", 40.77540400265574, -73.95544597256219, "restaurant", "Japanese sushi; Tejan rec"),
    ("Lower East Side for DJs", 40.71847031817319, -73.98782878404761, "activity", "Neighborhood with DJ venues; Tejan rec"),
    ("Elsewhere Club (Brooklyn)", 40.709770289078676, -73.92323097988586, "club/bar", "Brooklyn club with live music and DJs; Daisy rec"),
    ("Alphabet City Neighborhood", 40.72589660860112, -73.97934794707074, "activity", "Notable nightlife and arts district; Daisy rec"),
    ("Lovers of Today Bar", 40.7259961454154, -73.98345378662009, "club/bar", "Neighborhood bar; Daisy rec"),
    ("Staten Island Ferry", 40.70150400823482, -74.0133962307327, "activity", "Free ferry ride with Manhattan views"),
    ("The Strand Bookstore", 40.735510519379105, -73.99127337215997, "store", "Books and music; Tejan rec"),
    ("Fushimi Market", 40.74690639442177, -73.98977995779416, "restaurant", "Market near Strand; Tejan rec"),
    ("Central Park", 40.78268468080871, -73.96564777314906, "park", "Large city park with multiple activities; free"),
    ("Stonewall Inn", 40.73405210332597, -74.00214114245857, "club/bar", "Historic LGBTQ+ bar; schedule varies: bingo, piano, karaoke, drag, DJs"),
    ("National Museum of the American Indian", 40.70410810105897, -74.0136889000878, "museum", "Open daily; free admission"),
    ("Whitney Museum of American Art", 40.73975841010002, -74.00890581544209, "museum", "Contemporary art; free under 25"),
    ("Washington Square Park", 40.73112770333569, -73.99737491548636, "park", "Famous NYC park; Lucy rec"),
    ("McDougal Street", 40.73011236509266, -74.00062910194019, "activity", "Street with historic bars and venues; Lucy rec"),
    ("Tompkins Square Park", 40.726803509793726, -73.98171972714188, "park", "Neighborhood park; Wally rec"),
    ("Fort Greene Park", 40.6918389459963, -73.97511725421661, "park", "Neighborhood park; Wally rec"),
    ("National Jazz Museum in Harlem", 40.8102632403638, -73.9429838118673, "museum", "Open Thurs-Sat; suggested donation to enter"),
    ("Trinity Churchyard", 40.83318065248414, -73.94917304427814, "park", "Historic cemetery with notable burials including Hamilton"),
    ("Seaglass Carousel at Battery Park", 40.702340273361685, -74.01503408659397, "activity", "$6 per ride"),
    ("Brooklyn Botanical Garden", 40.66905178690165, -73.96449105786516, "activity", "$17 with student ID; closed Mondays"),
    ("Museum of the Moving Image", 40.75662171792481, -73.92397105785173, "museum", "$12 with student ID; free Thursday; screens film and media exhibits"),
    ("Noguchi Museum", 40.76712177720009, -73.93813973084133, "museum", "Art museum and sculpture garden; free the planned Friday, reserve two weeks ahead"),
    ("Fort Tilden Beach", 40.55995617267501, -73.88764728663617, "park", "Beach location; Daisy rec"),
    ("Bossa Nova Civic Club", 40.698236728746764, -73.92792190015818, "club/bar", "Brooklyn nightclub; Daisy rec"),
    ("Nowadays Bushwick Club", 40.692624596179975, -73.90149288478176, "club/bar", "Club in Bushwick; Daisy rec"),
    ("Brooklyn Steel Venue", 40.719422752244256, -73.93870806942547, "venue", "Concert venue; Daisy rec"),
    ("Brooklyn Monarch Venue", 40.71100688614372, -73.9361860424009, "venue", "Concert venue; Daisy rec"),
    ("Trans Pecos Club", 40.697391369495776, -73.90609366945495, "club/bar", "Sissies of Mercy LGBTQ+ club; Daisy rec"),
    ("Bushwick Collective (Graffiti Art Gallery)", 40.70763939460192, -73.92221668660602, "museum", "Free street art gallery"),
    ("Tannen's Magic Shop", 40.749863145031405, -73.98693502896411, "store", "Oldest magic shop in NYC; open daily except Sunday"),
    ("Central Park Boat Rental", 40.775271421051, -73.968752957798, "activity", "$25/hour rowboat rental"),
    ("Little Island Park", 40.742148717647076, -74.01036337310617, "park", "Elevated park on the Hudson River"),
    ("Little Italy", 40.71950524834782, -73.99723215806527, "activity", "Historic Italian neighborhood"),
    ("NYU (New York University)", 40.73453345870364, -73.9938532958971, "activity", "University campus"),
    ("TV Eye (Punk Venue)", 40.698008948869024, -73.90527214427885, "venue", "Punk venue"),
    ("McGee's Pub", 40.76503502313631, -73.98296081358961, "club/bar", "Pub that inspired How I Met Your Mother"),
    ("House of Yes", 40.70706222200007, -73.92358822649253, "club/bar", "Dance, circus, theater, cabaret venue"),
    ("Don't Tell Mama Piano Bar", 40.76074545024818, -73.98951822893927, "club/bar", "Theater and piano performances"),
    ("Pier 17 (Rooftop Concert)", 40.705608698004475, -74.00166425778005, "venue", "Rooftop concert venue"),
    ("Bedford Ave (Brooklyn)", 40.65396483008125, -73.95621201542403, "activity", "Brooklyn street with shops and restaurants; Lucy rec"),
    ("Carrie Bradshaw's Apartment (66 Perry St)", 40.73553929134069, -74.0039028154642, "activity", "Fictional apartment location from Sex and the City"),
    ("Daredevil Tattoo Museum", 40.714639370934364, -73.99094211546488, "museum", "Tattoo history in NYC; open during shop hours; free"),
    ("George Glazer Gallery", 40.78271580457388, -73.94736482705805, "museum", "Cartography store and gallery"),
    ("White Horse Tavern", 40.740640275674906, -74.00619200437554, "club/bar", "Historic Beat Generation bar"),
    ("Mercury Lounge", 40.72228143658013, -73.986778086596, "venue", "Live music venue"),
    ("Shakespeare in Central Park", 40.78070088555576, -73.96891357523388, "activity", "Outdoor Shakespeare performances"),
    ("Prospect Park Carousel", 40.66394291947269, -73.96429124427955, "activity", "Carousel featured in Now You See Me"),
    ("Times Square", 40.75808441191918, -73.98557478650923, "activity", "what even goes on here"),
    ("Empire State Building", 40.74858677489018, -73.98561075911327, "activity", "never heard of it"),
    ("Statue Of Liberty Lookout", 40.70147336438084, -74.01505412509248, "activity", "Free views of Statue of Liberty from Battery Park"),
    ("Summit One Vanderbilt", 40.75296965853865, -73.97866092708148, "activity", "Observation deck with city views; expensive"),
    ("Broadway (Hamilton or Cursed Child)", 40.76338654475623, -73.98307432707146, "venue", "Theater shows; lottery tickets recommended"),
    ("Hamilton Grange National Memorial", 40.82148228580702, -73.9472809424264, "museum", "Historic site; quiet uptown location"),
    ("Museum of Reclaimed Urban Space", 40.72599376064957, -73.9779247425263, "museum", "Urban activism museum; open Wed-Sun; $5 suggested donation"),
    ("Rubulad", 40.70467429999638, -73.92732352525321, "club/bar", "Art and live music venue"),
    ("Bronx Zoo", 40.850247001894914, -73.8767109712605, "activity", "Free Wednesdays; reserve Mondays at 5pm"),
    ("Summer on the Hudson (West Side County Fair)", 40.8000, -73.9600, "activity", "County fair event; Sunday Sept 7"),
    ("Ferragosto Italian Culture Celebration", 40.8000, -73.9600, "activity", "Italian cultural event; Sunday Sept 7"),
    ("Nonna's of the World", 40.64217707346529, -74.07723494057129, "restaurant", "International grandmas cooking; meals $50-100")
]



# Create the map
m = folium.Map(location=nyc_center, zoom_start=11)

# --- CLUSTERING AND CIRCLES ---
from sklearn.cluster import DBSCAN
import numpy as np

# Prepare coordinates for clustering
coords = np.array([(lat, lon) for _, lat, lon, _, _ in locations])

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


for idx, (name, lat, lon, loc_type, description) in enumerate(locations):
    color_idx = (idx - 1) // 12
    color = colors[color_idx] if color_idx < len(colors) else 'gray'
    icon_symbol = icon_map.get(loc_type, 'info-sign')
    popup_html = f"<div style='font-size:12px; width:300px'><b>{name}</b><br>{description}</div>"
    folium.Marker(
        [lat, lon],
        popup=popup_html,
        icon=folium.Icon(color=color, icon=icon_symbol)
    ).add_to(m)

# Save to HTML file
m.save("index.html")
print("Map saved as index.html")