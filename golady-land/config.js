/* ============================================================
   ✏️  CONFIG.JS — GOLADY SHOP
   Tu modifies UNIQUEMENT ce fichier pour chaque produit.
   Ne touche jamais à index.html
   ============================================================ */

var CONFIG = {

  /* ── INFOS PRODUIT ── */
  produit: {
    nom:        "Easy Move – Sandale",
    prix:       "6 250 DA",
    prix_barre: "7 450 DA",
    remise:     "−16%",
    stock:      8,

    /* ── DESCRIPTION ── */
    description: "Les Sandales Easy Move sont pensées pour la femme algérienne moderne — un design sobre, une stabilité parfaite et un confort qui vous accompagne tout au long de la journée. Elles allient simplicité et élégance pour un usage quotidien sans compromis.",

    /* ── CARACTÉRISTIQUES (icon + titre + description courte) ── */
    features: [
      { icon: "👠", titre: "Talon stable 6 cm",        desc: "Confort toute la journée sans fatigue" },
      { icon: "✨", titre: "Finition premium",          desc: "Matière soignée, brillance durable" },
      { icon: "🛡️", titre: "Semelle antidérapante",    desc: "Sécurité sur tous les sols" },
      { icon: "📐", titre: "Taille fidèle",             desc: "Commandez votre pointure habituelle" }
    ],

    /* ── GUIDE POINTURES ── */
    guide_pointures: [
      { pointure: "36", longueur: "22.5 cm" },
      { pointure: "37", longueur: "23.5 cm" },
      { pointure: "38", longueur: "24 cm"   },
      { pointure: "39", longueur: "24.5 cm" },
      { pointure: "40", longueur: "25 cm"   },
      { pointure: "41", longueur: "25.5 cm" }
    ],

    /* ── CONSEIL STYLE ── */
    conseil_style: "À porter avec un jean, une robe simple ou une tenue de travail. Ces sandales à talon moyen stable, avec leur bon maintien du pied et leur confort de marche, sont parfaites pour le quotidien, le travail et les longues journées actives."
  },

  /* ── CONTACT ── */
  contact: {
    whatsapp:  "213557190401",
    telephone: "0796960426"
  },

  /* ── RÉSEAUX SOCIAUX ── */
  social: {
    facebook:  "https://web.facebook.com/goladyshop.officiel",
    instagram: "https://www.instagram.com/golady_dz/"
  },

  /* ── PIXEL META ── */
  pixel_id: "182147210623375",

  /* ── COULEURS + PHOTOS + POINTURES ── */
  couleurs: [
    {
      nom: "Marron", hex: "#8B6348",
      photos: [
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/11_d1c0d361-4a0f-4dd1-a095-082a79b84629.png?v=1775261081",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/9_8afc6d63-60c7-4385-ac5e-0799963b7671.png?v=1776110141",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/8_25f3141d-8705-4489-a1e4-5c819c58b9ef.png?v=1775261162",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/7_c48f793c-0a0c-4934-beaf-14b390565fd2.png?v=1775261162",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/6_5629a910-1b3c-4aef-8f05-8f83962382b7.png?v=1775261162",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/4_f7d37a8a-9aba-422e-b16a-14f06f692e04.png?v=1776110141",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/3_eecc895b-e2d3-420f-9f1e-82250602e398.png?v=1776110141",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_2958219a-0ad0-422a-aa30-ee7b5247c2fd.png?v=1776110141"
      ],
      pointures: { disponibles: ["36","37","38","39","40","41"], epuisees: [] }
    },
    {
      nom: "Noir", hex: "#1a1a1a",
      photos: [
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/28_d454591b-82f1-47c2-977e-59cbd87380a7.png?v=1775259383",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/27_2af8fc50-026d-4306-9b8b-eecbc29dc99e.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/26_29cb7334-7d3a-4e67-a10d-b6ab60094c43.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/25_fd8f3388-30f8-4a30-ab81-53e52eabfdbd.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/24_c2ee82a6-1351-4f9d-baf4-a86341d6441d.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/23_1a35032d-b56f-4c55-b1d0-572a042b73e4.png?v=1775259383",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/20_ca0208de-de67-417d-accb-238dc9766854.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/14_5f46757a-15b6-4481-9852-dd6ea58e8607.png?v=1775259384",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/13_2354ef88-ef6c-4b9d-aa19-21fafe374d4c.png?v=1775259384"
      ],
      pointures: { disponibles: ["36","37","38","39","40","41"], epuisees: [] }
    },
    {
      nom: "Beige", hex: "#e6a980",
      photos: [
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/4_f734f5d4-77b8-48c2-8643-2a21af3b8fcd.png?v=1779048011",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/5_c983993a-3213-4050-9611-80eb9791e85d.png?v=1779048011",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/7_a04cd830-a1cd-43ab-9d72-00e2b41d1a04.png?v=1779048013",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_19dad3df-e5bd-4a9c-b502-515fb4d2e26a.png?v=1779048011",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/3_465e287f-c1ef-4e24-a031-b621b828ef13.png?v=1779048011",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/6_23eb15cf-4fab-4ef5-88d9-b9d5869aec60.png?v=1779048011"
      ],
      pointures: { disponibles: ["36","37","38","39","40","41"], epuisees: [] }
    },
    {
      nom: "Bordeaux", hex: "#852424",
      photos: [
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/3_425de49e-6b50-4749-af38-8d7abfcbaf05.png?v=1779055468",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/9_62ca5ca3-9edf-4895-85ab-606039cbaf4d.png?v=1779055465",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/2_9a3202b2-07fc-4a6e-9335-8e0894905be1.png?v=1779055464",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_c50a20a9-4822-47d0-89e9-e63ce53d2f8e.png?v=1779055463",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/13_ec074b7f-f492-4bb0-ba4d-6cd6c7e8b8bf.png?v=1779055461",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/10_af1f0cd5-ff8b-478e-b92a-2b4d2514b846.png?v=1779055460"
      ],
      pointures: { disponibles: ["36","37","38","39","40","41"], epuisees: [] }
    },
    {
      nom: "Blanc", hex: "#f0f0f0",
      photos: [
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_23c13371-99f1-45f2-880a-0072530ba389.png?v=1779048446",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/12_b3160ffc-6230-492a-8579-6d1cb15c94ff.png?v=1779048445",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/11_85c29bea-34a5-49d5-afc9-3540321a0f0a.png?v=1779048445",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/9_e1eec264-77b3-4cc8-b250-065af0ff8505.png?v=1779048443",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/15_ae9a7363-4355-4a0c-bfb6-865449e34476.png?v=1779048442",
        "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/8_a20b97ce-c744-465d-88d1-682d8a84589b.png?v=1779048444"
      ],
      pointures: { disponibles: ["36","37","38","39","40","41"], epuisees: [] }
    }
  ],

  /* ── AVIS CLIENTS ── */
  avis_photos: [
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/Design_sans_titre_20cb198b-f166-4ac4-adbe-952338200241.png?v=1778889558",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_062fb7bc-d7f9-409d-a0e6-f42dd250b2d5.png?v=1777721805",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/4_974cf235-8007-43d4-ab1e-76f344004264.png?v=1777721585",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/1_42661732-4077-4b44-a62c-d69853c97cac.png?v=1777721584",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/2_399c32d5-8d39-48d3-8949-34e2692cc306.png?v=1777721804",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/10_a6f34310-cf2d-4e13-aff9-96733534c1d9.png?v=1777817567",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/9_7f3e90b6-62cd-4da5-be97-0da722f2abd2.png?v=1777817566",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/6_e92ac24f-82f3-43e0-bf3c-bd0add314817.png?v=1777817566",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/4_24b93f88-5061-4b8a-9c05-7b9750a686b7.png?v=1777817566",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/5_179b121f-d869-4c8e-b6ff-7481643af4ad.png?v=1777817565",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/8_a6a620a5-c3a2-4162-a984-58b8481a13da.png?v=1777817564",
    "https://cdn.shopify.com/s/files/1/0021/3191/8935/files/7_18112fae-f578-43a2-82d8-d5e4abf46a8a.png?v=1777817564"
  ]

};
