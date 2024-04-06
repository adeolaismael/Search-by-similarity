import pytest
from src.extraction import process_pptx_files, extract_information

def test_extract_information():
    # Chemin vers un fichier PowerPoint de test ou un exemple simulé
    test_file_path = 'C:/Users/ed/Documents/Projet personnel machine learning/FASEP/Exemple_FASEP.pptx'

    # Utiliser process_pptx_files pour extraire le texte
    extracted_text = process_pptx_files([test_file_path])
    text = extracted_text[test_file_path]

    # Appel de extract_information avec le texte extrait 
    extracted_info = extract_information(text)

    # Dictionnaire des résultats attendus
    expected = {
        "Date de signature de la convention Natixis": "11 Septembre 2020",
        "Montant du FASEP": "400 000 €",
        "Montant de l'acompte": "100 000 euro",
        "Date de paiement de l'acompte": "24 Décembre 2020",
        "Avis du service économique pour le premier terme intermédiaire": "Favorable"
    }

    # Vérification que les données extraites correspondent aux données attendues
    assert extracted_info == expected
