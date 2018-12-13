{
    'name' : 'Exercice',
    'author' : 'FDL',
    'version' : '1.0',
    'summary': 'Exercice',
    'sequence': 15,
    'description': """
Exercice
====================
Installer l’application Sales Management
Créer un nouveau module nommé Exercice, puis dans ce module:
Ajouter un champ texte nommé « Exercice » sur l’objet sale.order dont le contenu doit être traduisible en anglais et français.
Afficher ce champ dans l’interface (via xml) après le champ nommé « note » du formulaire de vente
Afficher ce champ dans le rapport lié (quotation/sale order dans le menu imprimer).
Le contenu du champ doit être affiché dans la langue du client.
Ajouter la traduction du champ (via un fichier po)
Partager ce module sur GitHub en séparant l’ajout du module et les modifications dans des commits appropriés
Tout ajout supplémentaire (champ calculé, relation…) qui démontrera une recherche approfondie sera apprécié""",
	'category': 'Sales',
    'depends' : ['sale_management'],
    'data': [
        'views/sale_view.xml',
        'report/sale_report.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
  }
