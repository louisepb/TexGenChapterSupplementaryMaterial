# Create a textile
Textile = CTextile()

# Create a python list containing 4 yarns
Yarns = [CYarn(), CYarn(), CYarn(), CYarn()]

# Add nodes to the yarns to describe their paths
Yarns[0].AddNode(CNode(XYZ(0, 0, 0)))
Yarns[0].AddNode(CNode(XYZ(0.22, 0, 0.05)))
Yarns[0].AddNode(CNode(XYZ(0.44, 0, 0)))

Yarns[1].AddNode(CNode(XYZ(0, 0.22, 0.05)))
Yarns[1].AddNode(CNode(XYZ(0.22, 0.22, 0)))
Yarns[1].AddNode(CNode(XYZ(0.44, 0.22, 0.05)))

Yarns[2].AddNode(CNode(XYZ(0, 0, 0.05)))
Yarns[2].AddNode(CNode(XYZ(0, 0.22, 0)))
Yarns[2].AddNode(CNode(XYZ(0, 0.44, 0.05)))

Yarns[3].AddNode(CNode(XYZ(0.22, 0, 0)))
Yarns[3].AddNode(CNode(XYZ(0.22, 0.22, 0.05)))
Yarns[3].AddNode(CNode(XYZ(0.22, 0.44, 0)))

# Loop over all the yarns in the list
for Yarn in Yarns:

    # Set the interpolation function
    Yarn.AssignInterpolation(CInterpolationCubic())

    # Assign a constant cross-section along the yarn of elliptical shape
    Yarn.AssignSection(CYarnSectionConstant(CSectionEllipse(0.18, 0.04)))

    # Set the resolution of the mesh created
    Yarn.SetResolution(20)

    # Add repeat vectors to the yarn
    Yarn.AddRepeat(XYZ(0.44, 0, 0))
    Yarn.AddRepeat(XYZ(0, 0.44, 0))

    # Add the yarn to our textile
    Textile.AddYarn(Yarn)

# Create a domain and assign it to the textile
Textile.AssignDomain(CDomainPlanes(XYZ(0, 0, -0.02), XYZ(0.44, 0.44, 0.07)))

# Add the textile with the name "polyester"
AddTextile("polyester", Textile)