#Email template to send when the login is unsuccessful to the mail address of the user
#
email_body = """Ceci est un message automatique, Bonjour,
     Nous sommes désolés de vous informer que la connexion a échouée.
     Veuillez vérifier vos informations d'identification et re-envoyer le formulaire (pas besoin d'envoyer les liens, juste les identifiants correct pour le site). Pensez aussi à verifier que vos comptes soient remplis correctement (CV, numéro mobile, etc) et que vous nous envoyez des liens de recherche, et le lien d'une offre d'entreprise en particulier.
     Cordialement, L'équipe Toolazy """
email_subject = "Echec de Connexion a {website}"


gmail_sender_account = "candidatures@toolazy.fr"
gmail_sender_password = 'aaofpzcrxhpgobtj'

email_body_no_job = """Bonjour,
     Nous sommes désolés de vous informer qu'il n'y a pas d'emplois disponibles pour ce site, il peu s'agir de plusieurs raisons, les liens ne sont pas bons (exemple vous avez fournis le lien d'une offre au lieu d'un lien de recherche, ou que votre compte du site en question n'est pas completé comme il se doit (CV, etc) , ou simplement que les liens envoyés n'ont pas encore d'offres disponibles sur la plateforme (attention toolazy ne fonctionne pas avec les offres qui redirigent sur un site tiers).
     Veuillez verifier ces hypothèses et envoyer de nouveaux liens si besoin.
    
     Cordialement,
     L'équipe Toolazy"""

email_subject_no_job = "Aucune offre disponible pour {website}"
