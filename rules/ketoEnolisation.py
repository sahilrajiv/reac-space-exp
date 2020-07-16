ketoEnolisation = [ruleGMLString("""rule [
    ruleID "ketoEnolisation"
    left[
        edge [ source 1 target 2 label "=" ]
        edge [ source 1 target 3 label "-" ]
        edge [ source 3 target 4 label "-" ]
    ]
    context [
        node [ id 1 label "C" ]
        node [ id 2 label "O" ]
        node [ id 3 label "C" ]
        node [ id 4 label "H" ]
    ]
    right [
        edge [ source 1 target 3 label "=" ]
        edge [ source 1 target 2 label "-" ]
        edge [ source 2 target 4 label "-" ]
    ]
]
""")]