import os

print("Chargement des tweets...")
os.system("python /home/utilisateur/Documents/devia_2425/llm_project/twitter_extract_verbatims/load_tweets.py")

print("Nettoyage des tweets...")
os.system("python /home/utilisateur/Documents/devia_2425/llm_project/twitter_extract_verbatims/clean_tweets.py")

print("Pipeline terminée avec succès !")
