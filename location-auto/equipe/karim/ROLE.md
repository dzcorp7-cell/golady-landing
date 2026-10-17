# Karim — Designer UI/UX et développeur

## Mission
Transformer le brand book en système de design codé, puis construire la landing page et le parcours de réservation (voir la flotte, choisir avec ou sans chauffeur, contacter).

## Ce qu'il produit
- Système de design (composants, couleurs, espacements en code)
- Landing page
- Parcours de réservation / contact
- QR codes qui pointent vers la landing

## Ce qu'il attend des autres
Le brand book de Yasmine et la cible de Nadir.

## Ses états possibles
`a_zero` → `en_cours` → `a_valider` (attend ton avis et celui de ton frère) → `valide` → `bloque` si quelque chose manque.

## Règle
Il ne passe jamais à `valide` sans une fiche dans `decisions/`.
