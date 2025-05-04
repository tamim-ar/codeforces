n = int(input())
face_counts = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

total_faces = 0
for _ in range(n):
    polyhedron = input()
    total_faces += face_counts[polyhedron]

print(total_faces)
