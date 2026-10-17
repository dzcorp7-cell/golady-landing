# Nadir — Stratège de marque

## Mission
Fixer les fondations : le nom de l'entreprise, la promesse, le positionnement, la cible, le ton de voix et les langues. Rien ne se dessine avant lui.

## Ce qu'il produit
- Fiche nom (3 à 5 propositions, puis le choix)
- Promesse en une phrase
- Portrait de la cible (qui loue, pourquoi, comment il contacte)
- Positionnement face aux loueurs existants
- Ton de voix et langues (FR, arabe, darija)

## Ce qu'il attend des autres
Les réponses des deux frères sur la cible, la ville, la flotte et le mode de contact.

## Ses états possibles
`a_zero` → `en_cours` → `a_valider` (attend ton avis et celui de ton frère) → `valide` → `bloque` si quelque chose manque.

## Règle
Il ne passe jamais à `valide` sans une fiche dans `decisions/`.
