"""
Mock Data Store for Krishi Mitra API
"""

DISTRICTS = [
    {"id": "dist-nashik", "name": "Nashik", "marathi_name": "नाशिक"},
    {"id": "dist-pune", "name": "Pune", "marathi_name": "पुणे"},
    {"id": "dist-ahmednagar", "name": "Ahilyanagar (Ahmednagar)", "marathi_name": "अहिल्यानगर"},
    {"id": "dist-solapur", "name": "Solapur", "marathi_name": "सोलापूर"},
    {"id": "dist-satara", "name": "Satara", "marathi_name": "सातारा"},
    {"id": "dist-kolhapur", "name": "Kolhapur", "marathi_name": "कोल्हापूर"},
    {"id": "dist-sangli", "name": "Sangli", "marathi_name": "सांगली"},
    {"id": "dist-aurangabad", "name": "Chhatrapati Sambhajinagar", "marathi_name": "छत्रपती संभाजीनगर"},
    {"id": "dist-jalna", "name": "Jalna", "marathi_name": "जालना"},
    {"id": "dist-latur", "name": "Latur", "marathi_name": "लातूर"},
    {"id": "dist-nanded", "name": "Nanded", "marathi_name": "नांदेड"},
    {"id": "dist-parbhani", "name": "Parbhani", "marathi_name": "परभणी"},
    {"id": "dist-hingoli", "name": "Hingoli", "marathi_name": "हिंगोली"},
    {"id": "dist-beed", "name": "Beed", "marathi_name": "बीड"},
    {"id": "dist-osmanabad", "name": "Dharashiv", "marathi_name": "धाराशिव"},
    {"id": "dist-nagpur", "name": "Nagpur", "marathi_name": "नागपूर"},
    {"id": "dist-wardha", "name": "Wardha", "marathi_name": "वर्धा"},
    {"id": "dist-bhandara", "name": "Bhandara", "marathi_name": "भंडारा"},
    {"id": "dist-gondia", "name": "Gondia", "marathi_name": "गोंदिया"},
    {"id": "dist-chandrapur", "name": "Chandrapur", "marathi_name": "चंद्रपूर"},
    {"id": "dist-gadchiroli", "name": "Gadchiroli", "marathi_name": "गडचिरोली"},
    {"id": "dist-amravati", "name": "Amravati", "marathi_name": "अमरावती"},
    {"id": "dist-akola", "name": "Akola", "marathi_name": "अकोला"},
    {"id": "dist-buldhana", "name": "Buldhana", "marathi_name": "बुलढाणा"},
    {"id": "dist-washim", "name": "Washim", "marathi_name": "वाशीम"},
    {"id": "dist-yavatmal", "name": "Yavatmal", "marathi_name": "यवतमाळ"},
    {"id": "dist-dhule", "name": "Dhule", "marathi_name": "धुळे"},
    {"id": "dist-nandurbar", "name": "Nandurbar", "marathi_name": "नंदुरबार"},
    {"id": "dist-jalgaon", "name": "Jalgaon", "marathi_name": "जळगाव"},
    {"id": "dist-raigad", "name": "Raigad", "marathi_name": "रायगड"},
    {"id": "dist-ratnagiri", "name": "Ratnagiri", "marathi_name": "रत्नागिरी"},
    {"id": "dist-sindhudurg", "name": "Sindhudurg", "marathi_name": "सिंधुदुर्ग"},
    {"id": "dist-thane", "name": "Thane", "marathi_name": "ठाणे"},
    {"id": "dist-palghar", "name": "Palghar", "marathi_name": "पालघर"},
    {"id": "dist-mumbai-city", "name": "Mumbai City", "marathi_name": "मुंबई शहर"},
    {"id": "dist-mumbai-suburban", "name": "Mumbai Suburban", "marathi_name": "मुंबई उपनगर"}
]

TALUKAS = {
    "dist-nashik": [
        {
                "id": "tal-malegaon",
                "name": "Malegaon",
                "marathi_name": "मालेगाव"
        },
        {
                "id": "tal-nandgaon",
                "name": "Nandgaon",
                "marathi_name": "नांदगाव"
        },
        {
                "id": "tal-chandwad",
                "name": "Chandwad",
                "marathi_name": "चांदवड"
        },
        {
                "id": "tal-niphad",
                "name": "Niphad",
                "marathi_name": "निफाड"
        },
        {
                "id": "tal-yeola",
                "name": "Yeola",
                "marathi_name": "येवला"
        },
        {
                "id": "tal-sinnar",
                "name": "Sinnar",
                "marathi_name": "सिन्नर"
        },
        {
                "id": "tal-kalwan",
                "name": "Kalwan",
                "marathi_name": "कलवण"
        },
        {
                "id": "tal-satana",
                "name": "Baglan (Satana)",
                "marathi_name": "बागलाण (सटाणा)"
        }
],
    "dist-pune": [
        {"id": "tal-pune-city", "name": "Pune City", "marathi_name": "पुणे शहर"},
        {"id": "tal-haveli", "name": "Haveli", "marathi_name": "हवेली"},
        {"id": "tal-khed", "name": "Khed (Rajgurunagar)", "marathi_name": "खेड (राजगुरुनगर)"},
        {"id": "tal-baramati", "name": "Baramati", "marathi_name": "बारामती"},
        {"id": "tal-junnar", "name": "Junnar", "marathi_name": "जुन्नर"},
        {"id": "tal-shirur", "name": "Shirur", "marathi_name": "शिरूर"},
        {"id": "tal-indapur", "name": "Indapur", "marathi_name": "इंदापूर"},
        {"id": "tal-daund", "name": "Daund", "marathi_name": "दौंड"},
        {"id": "tal-mawal", "name": "Mawal", "marathi_name": "मावळ"},
        {"id": "tal-ambegaon", "name": "Ambegaon", "marathi_name": "आंबेगाव"},
        {"id": "tal-purandhar", "name": "Purandhar (Saswad)", "marathi_name": "पुरंदर (सासवड)"},
        {"id": "tal-bhor", "name": "Bhor", "marathi_name": "भोर"},
        {"id": "tal-mulshi", "name": "Mulshi (Paud)", "marathi_name": "मुळशी (पौड)"},
        {"id": "tal-velhe", "name": "Velhe (Rajgad)", "marathi_name": "वेल्हे (राजगड)"}
    ],
    "dist-jalna": [
        {"id": "tal-jalna", "name": "Jalna", "marathi_name": "जालना"},
        {"id": "tal-bhokardan", "name": "Bhokardan", "marathi_name": "भोकरदन"},
        {"id": "tal-jafrabad", "name": "Jafrabad", "marathi_name": "जाफ्राबाद"},
        {"id": "tal-badnapur", "name": "Badnapur", "marathi_name": "बदनापूर"},
        {"id": "tal-ambad", "name": "Ambad", "marathi_name": "अंबड"},
        {"id": "tal-ghansawangi", "name": "Ghansawangi", "marathi_name": "घनसावंगी"},
        {"id": "tal-partur", "name": "Partur", "marathi_name": "परतूर"},
        {"id": "tal-mantha", "name": "Mantha", "marathi_name": "मंठा"}
    ]
}

VILLAGES = {
    "tal-malegaon": [
        {
            "id": "vil-malegaon-aghar-bk",
            "name": "Aghar Bk",
            "marathi_name": "Aghar Bk"
        },
        {
            "id": "vil-malegaon-aghar-kh",
            "name": "Aghar Kh",
            "marathi_name": "Aghar Kh"
        },
        {
            "id": "vil-malegaon-ajande",
            "name": "Ajande",
            "marathi_name": "Ajande"
        },
        {
            "id": "vil-malegaon-ajande-kh",
            "name": "Ajande Kh",
            "marathi_name": "Ajande Kh"
        },
        {
            "id": "vil-malegaon-ajang",
            "name": "Ajang",
            "marathi_name": "Ajang"
        },
        {
            "id": "vil-malegaon-astane",
            "name": "Astane",
            "marathi_name": "Astane"
        },
        {
            "id": "vil-malegaon-belgaon",
            "name": "Belgaon",
            "marathi_name": "Belgaon"
        },
        {
            "id": "vil-malegaon-bharadenagar",
            "name": "Bharadenagar",
            "marathi_name": "Bharadenagar"
        },
        {
            "id": "vil-malegaon-bhayagaon",
            "name": "Bhayagaon",
            "marathi_name": "Bhayagaon"
        },
        {
            "id": "vil-malegaon-bhilkot",
            "name": "Bhilkot",
            "marathi_name": "Bhilkot"
        },
        {
            "id": "vil-malegaon-bhuigavhan",
            "name": "Bhuigavhan",
            "marathi_name": "Bhuigavhan"
        },
        {
            "id": "vil-malegaon-bodhe",
            "name": "Bodhe",
            "marathi_name": "Bodhe"
        },
        {
            "id": "vil-malegaon-chandanpuri",
            "name": "Chandanpuri",
            "marathi_name": "Chandanpuri"
        },
        {
            "id": "vil-malegaon-chaukatpada",
            "name": "Chaukatpada",
            "marathi_name": "Chaukatpada"
        },
        {
            "id": "vil-malegaon-chikhalohal",
            "name": "Chikhalohal",
            "marathi_name": "Chikhalohal"
        },
        {
            "id": "vil-malegaon-chinchagavhan",
            "name": "Chinchagavhan",
            "marathi_name": "Chinchagavhan"
        },
        {
            "id": "vil-malegaon-chinchavad",
            "name": "Chinchavad",
            "marathi_name": "Chinchavad"
        },
        {
            "id": "vil-malegaon-chinchave-galane",
            "name": "Chinchave (Galane)",
            "marathi_name": "Chinchave (Galane)"
        },
        {
            "id": "vil-malegaon-chondhi",
            "name": "Chondhi",
            "marathi_name": "Chondhi"
        },
        {
            "id": "vil-malegaon-dabhadi",
            "name": "Dabhadi",
            "marathi_name": "Dabhadi"
        },
        {
            "id": "vil-malegaon-dabli",
            "name": "Dabli",
            "marathi_name": "Dabli"
        },
        {
            "id": "vil-malegaon-dahidi",
            "name": "Dahidi",
            "marathi_name": "Dahidi"
        },
        {
            "id": "vil-malegaon-dahikute",
            "name": "Dahikute",
            "marathi_name": "Dahikute"
        },
        {
            "id": "vil-malegaon-dahiwal",
            "name": "Dahiwal",
            "marathi_name": "Dahiwal"
        },
        {
            "id": "vil-malegaon-dapur",
            "name": "Dapur",
            "marathi_name": "Dapur"
        },
        {
            "id": "vil-malegaon-daregaon",
            "name": "Daregaon",
            "marathi_name": "Daregaon"
        },
        {
            "id": "vil-malegaon-dasane",
            "name": "Dasane",
            "marathi_name": "Dasane"
        },
        {
            "id": "vil-malegaon-deoghat",
            "name": "Deoghat",
            "marathi_name": "Deoghat"
        },
        {
            "id": "vil-malegaon-devarpada",
            "name": "Devarpada",
            "marathi_name": "Devarpada"
        },
        {
            "id": "vil-malegaon-dhavali-vihir",
            "name": "Dhavali Vihir",
            "marathi_name": "Dhavali Vihir"
        },
        {
            "id": "vil-malegaon-dongrale",
            "name": "Dongrale",
            "marathi_name": "Dongrale"
        },
        {
            "id": "vil-malegaon-dubagule",
            "name": "Dubagule",
            "marathi_name": "Dubagule"
        },
        {
            "id": "vil-malegaon-dundhe",
            "name": "Dundhe",
            "marathi_name": "Dundhe"
        },
        {
            "id": "vil-malegaon-dyane",
            "name": "Dyane",
            "marathi_name": "Dyane"
        },
        {
            "id": "vil-malegaon-erandgaon",
            "name": "Erandgaon",
            "marathi_name": "Erandgaon"
        },
        {
            "id": "vil-malegaon-galne",
            "name": "Galne",
            "marathi_name": "Galne"
        },
        {
            "id": "vil-malegaon-ganeshnagar-mitranagar",
            "name": "Ganeshnagar (Mitranagar)",
            "marathi_name": "Ganeshnagar (Mitranagar)"
        },
        {
            "id": "vil-malegaon-garbad",
            "name": "Garbad",
            "marathi_name": "Garbad"
        },
        {
            "id": "vil-malegaon-garegaon",
            "name": "Garegaon",
            "marathi_name": "Garegaon"
        },
        {
            "id": "vil-malegaon-ghanegaon",
            "name": "Ghanegaon",
            "marathi_name": "Ghanegaon"
        },
        {
            "id": "vil-malegaon-ghodegaon",
            "name": "Ghodegaon",
            "marathi_name": "Ghodegaon"
        },
        {
            "id": "vil-malegaon-ghodegaonchoki",
            "name": "Ghodegaonchoki",
            "marathi_name": "Ghodegaonchoki"
        },
        {
            "id": "vil-malegaon-gigaon",
            "name": "Gigaon",
            "marathi_name": "Gigaon"
        },
        {
            "id": "vil-malegaon-gilane",
            "name": "Gilane",
            "marathi_name": "Gilane"
        },
        {
            "id": "vil-malegaon-gugulwad",
            "name": "Gugulwad",
            "marathi_name": "Gugulwad"
        },
        {
            "id": "vil-malegaon-hatane",
            "name": "Hatane",
            "marathi_name": "Hatane"
        },
        {
            "id": "vil-malegaon-hiswal-bk",
            "name": "Hiswal Bk",
            "marathi_name": "Hiswal Bk"
        },
        {
            "id": "vil-malegaon-jalgaon-galane",
            "name": "Jalgaon (Galane)",
            "marathi_name": "Jalgaon (Galane)"
        },
        {
            "id": "vil-malegaon-jalgaon-nimbait",
            "name": "Jalgaon (Nimbait)",
            "marathi_name": "Jalgaon (Nimbait)"
        },
        {
            "id": "vil-malegaon-jalku",
            "name": "Jalku",
            "marathi_name": "Jalku"
        },
        {
            "id": "vil-malegaon-jatpade",
            "name": "Jatpade",
            "marathi_name": "Jatpade"
        },
        {
            "id": "vil-malegaon-jeur",
            "name": "Jeur",
            "marathi_name": "Jeur"
        },
        {
            "id": "vil-malegaon-jwardi-bk",
            "name": "Jwardi Bk",
            "marathi_name": "Jwardi Bk"
        },
        {
            "id": "vil-malegaon-jwardi-kh",
            "name": "Jwardi Kh",
            "marathi_name": "Jwardi Kh"
        },
        {
            "id": "vil-malegaon-kajwade",
            "name": "Kajwade",
            "marathi_name": "Kajwade"
        },
        {
            "id": "vil-malegaon-kalewadi",
            "name": "Kalewadi",
            "marathi_name": "Kalewadi"
        },
        {
            "id": "vil-malegaon-kalwadi",
            "name": "Kalwadi",
            "marathi_name": "Kalwadi"
        },
        {
            "id": "vil-malegaon-kandhane",
            "name": "Kandhane",
            "marathi_name": "Kandhane"
        },
        {
            "id": "vil-malegaon-kankrale",
            "name": "Kankrale",
            "marathi_name": "Kankrale"
        },
        {
            "id": "vil-malegaon-karanj-gavhan",
            "name": "Karanj Gavhan",
            "marathi_name": "Karanj Gavhan"
        },
        {
            "id": "vil-malegaon-kashti",
            "name": "Kashti",
            "marathi_name": "Kashti"
        },
        {
            "id": "vil-malegaon-kaulane-galane",
            "name": "Kaulane (Galane)",
            "marathi_name": "Kaulane (Galane)"
        },
        {
            "id": "vil-malegaon-kaulane-n",
            "name": "Kaulane (N)",
            "marathi_name": "Kaulane (N)"
        },
        {
            "id": "vil-malegaon-khadaki",
            "name": "Khadaki",
            "marathi_name": "Khadaki"
        },
        {
            "id": "vil-malegaon-khakurdi",
            "name": "Khakurdi",
            "marathi_name": "Khakurdi"
        },
        {
            "id": "vil-malegaon-khalane",
            "name": "Khalane",
            "marathi_name": "Khalane"
        },
        {
            "id": "vil-malegaon-khayade",
            "name": "Khayade",
            "marathi_name": "Khayade"
        },
        {
            "id": "vil-malegaon-kothare-bk",
            "name": "Kothare Bk",
            "marathi_name": "Kothare Bk"
        },
        {
            "id": "vil-malegaon-kothare-kh",
            "name": "Kothare Kh",
            "marathi_name": "Kothare Kh"
        },
        {
            "id": "vil-malegaon-kukane",
            "name": "Kukane",
            "marathi_name": "Kukane"
        },
        {
            "id": "vil-malegaon-lakhani",
            "name": "Lakhani",
            "marathi_name": "Lakhani"
        },
        {
            "id": "vil-malegaon-lendane",
            "name": "Lendane",
            "marathi_name": "Lendane"
        },
        {
            "id": "vil-malegaon-lonwade",
            "name": "Lonwade",
            "marathi_name": "Lonwade"
        },
        {
            "id": "vil-malegaon-lulle",
            "name": "Lulle",
            "marathi_name": "Lulle"
        },
        {
            "id": "vil-malegaon-malagaon",
            "name": "Malagaon",
            "marathi_name": "Malagaon"
        },
        {
            "id": "vil-malegaon-maldhe",
            "name": "Maldhe",
            "marathi_name": "Maldhe"
        },
        {
            "id": "vil-malegaon-malegaon-m-corp-og",
            "name": "Malegaon (M Corp + OG)",
            "marathi_name": "Malegaon (M Corp + OG)"
        },
        {
            "id": "vil-malegaon-malhanagaon",
            "name": "Malhanagaon",
            "marathi_name": "Malhanagaon"
        },
        {
            "id": "vil-malegaon-manjare",
            "name": "Manjare",
            "marathi_name": "Manjare"
        },
        {
            "id": "vil-malegaon-manke",
            "name": "Manke",
            "marathi_name": "Manke"
        },
        {
            "id": "vil-malegaon-mathurpada",
            "name": "Mathurpada",
            "marathi_name": "Mathurpada"
        },
        {
            "id": "vil-malegaon-mehune",
            "name": "Mehune",
            "marathi_name": "Mehune"
        },
        {
            "id": "vil-malegaon-mohapada",
            "name": "Mohapada",
            "marathi_name": "Mohapada"
        },
        {
            "id": "vil-malegaon-mordar",
            "name": "Mordar",
            "marathi_name": "Mordar"
        },
        {
            "id": "vil-malegaon-mungase",
            "name": "Mungase",
            "marathi_name": "Mungase"
        },
        {
            "id": "vil-malegaon-nagaon-d",
            "name": "Nagaon (D)",
            "marathi_name": "Nagaon (D)"
        },
        {
            "id": "vil-malegaon-nagzari",
            "name": "Nagzari",
            "marathi_name": "Nagzari"
        },
        {
            "id": "vil-malegaon-nale",
            "name": "Nale",
            "marathi_name": "Nale"
        },
        {
            "id": "vil-malegaon-nandgaon",
            "name": "Nandgaon",
            "marathi_name": "Nandgaon"
        },
        {
            "id": "vil-malegaon-nandgaon-kh",
            "name": "Nandgaon Kh",
            "marathi_name": "Nandgaon Kh"
        },
        {
            "id": "vil-malegaon-nardane",
            "name": "Nardane",
            "marathi_name": "Nardane"
        },
        {
            "id": "vil-malegaon-nilgavhan",
            "name": "Nilgavhan",
            "marathi_name": "Nilgavhan"
        },
        {
            "id": "vil-malegaon-nimbait",
            "name": "Nimbait",
            "marathi_name": "Nimbait"
        },
        {
            "id": "vil-malegaon-nimgaon",
            "name": "Nimgaon",
            "marathi_name": "Nimgaon"
        },
        {
            "id": "vil-malegaon-nimgaon-kh",
            "name": "Nimgaon Kh",
            "marathi_name": "Nimgaon Kh"
        },
        {
            "id": "vil-malegaon-nimgule",
            "name": "Nimgule",
            "marathi_name": "Nimgule"
        },
        {
            "id": "vil-malegaon-nimgulekupa",
            "name": "Nimgulekupa",
            "marathi_name": "Nimgulekupa"
        },
        {
            "id": "vil-malegaon-nimshevadi",
            "name": "Nimshevadi",
            "marathi_name": "Nimshevadi"
        },
        {
            "id": "vil-malegaon-padalde",
            "name": "Padalde",
            "marathi_name": "Padalde"
        },
        {
            "id": "vil-malegaon-palasdare",
            "name": "Palasdare",
            "marathi_name": "Palasdare"
        },
        {
            "id": "vil-malegaon-pandharun",
            "name": "Pandharun",
            "marathi_name": "Pandharun"
        },
        {
            "id": "vil-malegaon-patane",
            "name": "Patane",
            "marathi_name": "Patane"
        },
        {
            "id": "vil-malegaon-patharde",
            "name": "Patharde",
            "marathi_name": "Patharde"
        },
        {
            "id": "vil-malegaon-pimpalgaon",
            "name": "Pimpalgaon",
            "marathi_name": "Pimpalgaon"
        },
        {
            "id": "vil-malegaon-pohane",
            "name": "Pohane",
            "marathi_name": "Pohane"
        },
        {
            "id": "vil-malegaon-rajmane",
            "name": "Rajmane",
            "marathi_name": "Rajmane"
        },
        {
            "id": "vil-malegaon-rampura",
            "name": "Rampura",
            "marathi_name": "Rampura"
        },
        {
            "id": "vil-malegaon-ravalgaon",
            "name": "Ravalgaon",
            "marathi_name": "Ravalgaon"
        },
        {
            "id": "vil-malegaon-ronzane",
            "name": "Ronzane",
            "marathi_name": "Ronzane"
        },
        {
            "id": "vil-malegaon-roze",
            "name": "Roze",
            "marathi_name": "Roze"
        },
        {
            "id": "vil-malegaon-sajvahal",
            "name": "Sajvahal",
            "marathi_name": "Sajvahal"
        },
        {
            "id": "vil-malegaon-sakur",
            "name": "Sakur",
            "marathi_name": "Sakur"
        },
        {
            "id": "vil-malegaon-sakuri-nimbait",
            "name": "Sakuri (Nimbait)",
            "marathi_name": "Sakuri (Nimbait)"
        },
        {
            "id": "vil-malegaon-sangameshwar",
            "name": "Sangameshwar",
            "marathi_name": "Sangameshwar"
        },
        {
            "id": "vil-malegaon-satarpada",
            "name": "Satarpada",
            "marathi_name": "Satarpada"
        },
        {
            "id": "vil-malegaon-satmane",
            "name": "Satmane",
            "marathi_name": "Satmane"
        },
        {
            "id": "vil-malegaon-saundane",
            "name": "Saundane",
            "marathi_name": "Saundane"
        },
        {
            "id": "vil-malegaon-savandgaon",
            "name": "Savandgaon",
            "marathi_name": "Savandgaon"
        },
        {
            "id": "vil-malegaon-savkarwadi",
            "name": "Savkarwadi",
            "marathi_name": "Savkarwadi"
        },
        {
            "id": "vil-malegaon-sawatawadi",
            "name": "Sawatawadi",
            "marathi_name": "Sawatawadi"
        },
        {
            "id": "vil-malegaon-sayane-bk",
            "name": "Sayane Bk",
            "marathi_name": "Sayane Bk"
        },
        {
            "id": "vil-malegaon-sayane-kh",
            "name": "Sayane Kh",
            "marathi_name": "Sayane Kh"
        },
        {
            "id": "vil-malegaon-shendurni",
            "name": "Shendurni",
            "marathi_name": "Shendurni"
        },
        {
            "id": "vil-malegaon-sherul",
            "name": "Sherul",
            "marathi_name": "Sherul"
        },
        {
            "id": "vil-malegaon-shirsondi",
            "name": "Shirsondi",
            "marathi_name": "Shirsondi"
        },
        {
            "id": "vil-malegaon-sitane",
            "name": "Sitane",
            "marathi_name": "Sitane"
        },
        {
            "id": "vil-malegaon-sonaj",
            "name": "Sonaj",
            "marathi_name": "Sonaj"
        },
        {
            "id": "vil-malegaon-soyagaon",
            "name": "Soyagaon",
            "marathi_name": "Soyagaon"
        },
        {
            "id": "vil-malegaon-takali",
            "name": "Takali",
            "marathi_name": "Takali"
        },
        {
            "id": "vil-malegaon-talwade",
            "name": "Talwade",
            "marathi_name": "Talwade"
        },
        {
            "id": "vil-malegaon-tehare",
            "name": "Tehare",
            "marathi_name": "Tehare"
        },
        {
            "id": "vil-malegaon-tingri",
            "name": "Tingri",
            "marathi_name": "Tingri"
        },
        {
            "id": "vil-malegaon-tipe",
            "name": "Tipe",
            "marathi_name": "Tipe"
        },
        {
            "id": "vil-malegaon-tokade",
            "name": "Tokade",
            "marathi_name": "Tokade"
        },
        {
            "id": "vil-malegaon-umbardhe",
            "name": "Umbardhe",
            "marathi_name": "Umbardhe"
        },
        {
            "id": "vil-malegaon-vadel",
            "name": "Vadel",
            "marathi_name": "Vadel"
        },
        {
            "id": "vil-malegaon-vadgaon",
            "name": "Vadgaon",
            "marathi_name": "Vadgaon"
        },
        {
            "id": "vil-malegaon-vadner",
            "name": "Vadner",
            "marathi_name": "Vadner"
        },
        {
            "id": "vil-malegaon-vajirkhede",
            "name": "Vajirkhede",
            "marathi_name": "Vajirkhede"
        },
        {
            "id": "vil-malegaon-vake",
            "name": "Vake",
            "marathi_name": "Vake"
        },
        {
            "id": "vil-malegaon-valwade",
            "name": "Valwade",
            "marathi_name": "Valwade"
        },
        {
            "id": "vil-malegaon-valwadi",
            "name": "Valwadi",
            "marathi_name": "Valwadi"
        },
        {
            "id": "vil-malegaon-vanpat",
            "name": "Vanpat",
            "marathi_name": "Vanpat"
        },
        {
            "id": "vil-malegaon-varhane",
            "name": "Varhane",
            "marathi_name": "Varhane"
        },
        {
            "id": "vil-malegaon-varhanepada",
            "name": "Varhanepada",
            "marathi_name": "Varhanepada"
        },
        {
            "id": "vil-malegaon-virane",
            "name": "Virane",
            "marathi_name": "Virane"
        },
        {
            "id": "vil-malegaon-yesgaon-bk",
            "name": "Yesgaon Bk",
            "marathi_name": "Yesgaon Bk"
        },
        {
            "id": "vil-malegaon-yesgaon-kh",
            "name": "Yesgaon Kh",
            "marathi_name": "Yesgaon Kh"
        },
        {
            "id": "vil-malegaon-zadi",
            "name": "Zadi",
            "marathi_name": "Zadi"
        },
        {
            "id": "vil-malegaon-zodge",
            "name": "Zodge",
            "marathi_name": "Zodge"
        }
    ],
    "tal-nandgaon": [
        {
            "id": "vil-nandgaon-amode",
            "name": "Amode",
            "marathi_name": "Amode"
        },
        {
            "id": "vil-nandgaon-anakwade",
            "name": "Anakwade",
            "marathi_name": "Anakwade"
        },
        {
            "id": "vil-nandgaon-astagaon",
            "name": "Astagaon",
            "marathi_name": "Astagaon"
        },
        {
            "id": "vil-nandgaon-aswaldara",
            "name": "Aswaldara",
            "marathi_name": "Aswaldara"
        },
        {
            "id": "vil-nandgaon-azadnagar",
            "name": "Azadnagar",
            "marathi_name": "Azadnagar"
        },
        {
            "id": "vil-nandgaon-babhulwadi",
            "name": "Babhulwadi",
            "marathi_name": "Babhulwadi"
        },
        {
            "id": "vil-nandgaon-bangaon-bk",
            "name": "Bangaon Bk",
            "marathi_name": "Bangaon Bk"
        },
        {
            "id": "vil-nandgaon-bangaon-kh",
            "name": "Bangaon Kh",
            "marathi_name": "Bangaon Kh"
        },
        {
            "id": "vil-nandgaon-besgaon",
            "name": "Besgaon",
            "marathi_name": "Besgaon"
        },
        {
            "id": "vil-nandgaon-bhalur",
            "name": "Bhalur",
            "marathi_name": "Bhalur"
        },
        {
            "id": "vil-nandgaon-bhardi",
            "name": "Bhardi",
            "marathi_name": "Bhardi"
        },
        {
            "id": "vil-nandgaon-bhauri",
            "name": "Bhauri",
            "marathi_name": "Bhauri"
        },
        {
            "id": "vil-nandgaon-birole",
            "name": "Birole",
            "marathi_name": "Birole"
        },
        {
            "id": "vil-nandgaon-bolthan",
            "name": "Bolthan",
            "marathi_name": "Bolthan"
        },
        {
            "id": "vil-nandgaon-borale",
            "name": "Borale",
            "marathi_name": "Borale"
        },
        {
            "id": "vil-nandgaon-boygaon",
            "name": "Boygaon",
            "marathi_name": "Boygaon"
        },
        {
            "id": "vil-nandgaon-chandanpuri",
            "name": "Chandanpuri",
            "marathi_name": "Chandanpuri"
        },
        {
            "id": "vil-nandgaon-chandore",
            "name": "Chandore",
            "marathi_name": "Chandore"
        },
        {
            "id": "vil-nandgaon-chinchvihir",
            "name": "Chinchvihir",
            "marathi_name": "Chinchvihir"
        },
        {
            "id": "vil-nandgaon-dahigaon",
            "name": "Dahigaon",
            "marathi_name": "Dahigaon"
        },
        {
            "id": "vil-nandgaon-darhel",
            "name": "Darhel",
            "marathi_name": "Darhel"
        },
        {
            "id": "vil-nandgaon-dhaner",
            "name": "Dhaner",
            "marathi_name": "Dhaner"
        },
        {
            "id": "vil-nandgaon-dheku-bk",
            "name": "Dheku Bk",
            "marathi_name": "Dheku Bk"
        },
        {
            "id": "vil-nandgaon-dheku-kh",
            "name": "Dheku Kh",
            "marathi_name": "Dheku Kh"
        },
        {
            "id": "vil-nandgaon-dhotane-bk",
            "name": "Dhotane Bk",
            "marathi_name": "Dhotane Bk"
        },
        {
            "id": "vil-nandgaon-dhotane-kh",
            "name": "Dhotane Kh",
            "marathi_name": "Dhotane Kh"
        },
        {
            "id": "vil-nandgaon-doctorwadi",
            "name": "Doctorwadi",
            "marathi_name": "Doctorwadi"
        },
        {
            "id": "vil-nandgaon-ekwai",
            "name": "Ekwai",
            "marathi_name": "Ekwai"
        },
        {
            "id": "vil-nandgaon-ganeshnagar",
            "name": "Ganeshnagar",
            "marathi_name": "Ganeshnagar"
        },
        {
            "id": "vil-nandgaon-gangadhari",
            "name": "Gangadhari",
            "marathi_name": "Gangadhari"
        },
        {
            "id": "vil-nandgaon-ghadeghewadi",
            "name": "Ghadeghewadi",
            "marathi_name": "Ghadeghewadi"
        },
        {
            "id": "vil-nandgaon-girnanagar",
            "name": "Girnanagar",
            "marathi_name": "Girnanagar"
        },
        {
            "id": "vil-nandgaon-gondegaon",
            "name": "Gondegaon",
            "marathi_name": "Gondegaon"
        },
        {
            "id": "vil-nandgaon-hingane-dehere",
            "name": "Hingane Dehere",
            "marathi_name": "Hingane Dehere"
        },
        {
            "id": "vil-nandgaon-hinganwadi",
            "name": "Hinganwadi",
            "marathi_name": "Hinganwadi"
        },
        {
            "id": "vil-nandgaon-hirenagar",
            "name": "Hirenagar",
            "marathi_name": "Hirenagar"
        },
        {
            "id": "vil-nandgaon-hiswal-bk",
            "name": "Hiswal Bk",
            "marathi_name": "Hiswal Bk"
        },
        {
            "id": "vil-nandgaon-hiswal-kh",
            "name": "Hiswal Kh",
            "marathi_name": "Hiswal Kh"
        },
        {
            "id": "vil-nandgaon-jalgaon-bk",
            "name": "Jalgaon Bk",
            "marathi_name": "Jalgaon Bk"
        },
        {
            "id": "vil-nandgaon-jalgaon-kh",
            "name": "Jalgaon Kh",
            "marathi_name": "Jalgaon Kh"
        },
        {
            "id": "vil-nandgaon-jamdari",
            "name": "Jamdari",
            "marathi_name": "Jamdari"
        },
        {
            "id": "vil-nandgaon-jategaon",
            "name": "Jategaon",
            "marathi_name": "Jategaon"
        },
        {
            "id": "vil-nandgaon-jawalki",
            "name": "Jawalki",
            "marathi_name": "Jawalki"
        },
        {
            "id": "vil-nandgaon-kalamdari",
            "name": "Kalamdari",
            "marathi_name": "Kalamdari"
        },
        {
            "id": "vil-nandgaon-karhi",
            "name": "Karhi",
            "marathi_name": "Karhi"
        },
        {
            "id": "vil-nandgaon-kasabkhede",
            "name": "Kasabkhede",
            "marathi_name": "Kasabkhede"
        },
        {
            "id": "vil-nandgaon-kasari",
            "name": "Kasari",
            "marathi_name": "Kasari"
        },
        {
            "id": "vil-nandgaon-khadgaon",
            "name": "Khadgaon",
            "marathi_name": "Khadgaon"
        },
        {
            "id": "vil-nandgaon-khirdipatode",
            "name": "Khirdipatode",
            "marathi_name": "Khirdipatode"
        },
        {
            "id": "vil-nandgaon-kondhar",
            "name": "Kondhar",
            "marathi_name": "Kondhar"
        },
        {
            "id": "vil-nandgaon-krantinagar",
            "name": "Krantinagar",
            "marathi_name": "Krantinagar"
        },
        {
            "id": "vil-nandgaon-kusumtel",
            "name": "Kusumtel",
            "marathi_name": "Kusumtel"
        },
        {
            "id": "vil-nandgaon-laxminagar",
            "name": "Laxminagar",
            "marathi_name": "Laxminagar"
        },
        {
            "id": "vil-nandgaon-lodhare",
            "name": "Lodhare",
            "marathi_name": "Lodhare"
        },
        {
            "id": "vil-nandgaon-lohashingve",
            "name": "Lohashingve",
            "marathi_name": "Lohashingve"
        },
        {
            "id": "vil-nandgaon-malaharwadi",
            "name": "Malaharwadi",
            "marathi_name": "Malaharwadi"
        },
        {
            "id": "vil-nandgaon-malegaon-karyat",
            "name": "Malegaon Karyat",
            "marathi_name": "Malegaon Karyat"
        },
        {
            "id": "vil-nandgaon-malgaon",
            "name": "Malgaon",
            "marathi_name": "Malgaon"
        },
        {
            "id": "vil-nandgaon-mandwad",
            "name": "Mandwad",
            "marathi_name": "Mandwad"
        },
        {
            "id": "vil-nandgaon-mangalane",
            "name": "Mangalane",
            "marathi_name": "Mangalane"
        },
        {
            "id": "vil-nandgaon-manikpunj",
            "name": "Manikpunj",
            "marathi_name": "Manikpunj"
        },
        {
            "id": "vil-nandgaon-manmad-m-cl",
            "name": "Manmad (M Cl)",
            "marathi_name": "Manmad (M Cl)"
        },
        {
            "id": "vil-nandgaon-mohegaon",
            "name": "Mohegaon",
            "marathi_name": "Mohegaon"
        },
        {
            "id": "vil-nandgaon-morzar",
            "name": "Morzar",
            "marathi_name": "Morzar"
        },
        {
            "id": "vil-nandgaon-muldongari",
            "name": "Muldongari",
            "marathi_name": "Muldongari"
        },
        {
            "id": "vil-nandgaon-nagapur",
            "name": "Nagapur",
            "marathi_name": "Nagapur"
        },
        {
            "id": "vil-nandgaon-nandgaon-m-cl",
            "name": "Nandgaon (M Cl)",
            "marathi_name": "Nandgaon (M Cl)"
        },
        {
            "id": "vil-nandgaon-nandgaon-rural",
            "name": "Nandgaon Rural",
            "marathi_name": "Nandgaon Rural"
        },
        {
            "id": "vil-nandgaon-nandur",
            "name": "Nandur",
            "marathi_name": "Nandur"
        },
        {
            "id": "vil-nandgaon-narayangaon",
            "name": "Narayangaon",
            "marathi_name": "Narayangaon"
        },
        {
            "id": "vil-nandgaon-nawasari",
            "name": "Nawasari",
            "marathi_name": "Nawasari"
        },
        {
            "id": "vil-nandgaon-naydongari",
            "name": "Naydongari",
            "marathi_name": "Naydongari"
        },
        {
            "id": "vil-nandgaon-new-panzan",
            "name": "New Panzan",
            "marathi_name": "New Panzan"
        },
        {
            "id": "vil-nandgaon-palshi",
            "name": "Palshi",
            "marathi_name": "Palshi"
        },
        {
            "id": "vil-nandgaon-panewadi",
            "name": "Panewadi",
            "marathi_name": "Panewadi"
        },
        {
            "id": "vil-nandgaon-panzandeo",
            "name": "Panzandeo",
            "marathi_name": "Panzandeo"
        },
        {
            "id": "vil-nandgaon-pardhadi",
            "name": "Pardhadi",
            "marathi_name": "Pardhadi"
        },
        {
            "id": "vil-nandgaon-parekarwadi",
            "name": "Parekarwadi",
            "marathi_name": "Parekarwadi"
        },
        {
            "id": "vil-nandgaon-phulenagar",
            "name": "Phulenagar",
            "marathi_name": "Phulenagar"
        },
        {
            "id": "vil-nandgaon-pimparkhed",
            "name": "Pimparkhed",
            "marathi_name": "Pimparkhed"
        },
        {
            "id": "vil-nandgaon-pimprale",
            "name": "Pimprale",
            "marathi_name": "Pimprale"
        },
        {
            "id": "vil-nandgaon-pimpri-haveli",
            "name": "Pimpri Haveli",
            "marathi_name": "Pimpri Haveli"
        },
        {
            "id": "vil-nandgaon-pohi",
            "name": "Pohi",
            "marathi_name": "Pohi"
        },
        {
            "id": "vil-nandgaon-pokhari-patode",
            "name": "Pokhari Patode",
            "marathi_name": "Pokhari Patode"
        },
        {
            "id": "vil-nandgaon-rankhede",
            "name": "Rankhede",
            "marathi_name": "Rankhede"
        },
        {
            "id": "vil-nandgaon-rohile-bk",
            "name": "Rohile Bk",
            "marathi_name": "Rohile Bk"
        },
        {
            "id": "vil-nandgaon-sakore",
            "name": "Sakore",
            "marathi_name": "Sakore"
        },
        {
            "id": "vil-nandgaon-satane",
            "name": "Satane",
            "marathi_name": "Satane"
        },
        {
            "id": "vil-nandgaon-sawargaon",
            "name": "Sawargaon",
            "marathi_name": "Sawargaon"
        },
        {
            "id": "vil-nandgaon-shastrinager",
            "name": "Shastrinager",
            "marathi_name": "Shastrinager"
        },
        {
            "id": "vil-nandgaon-shriramnagar",
            "name": "Shriramnagar",
            "marathi_name": "Shriramnagar"
        },
        {
            "id": "vil-nandgaon-soygaon",
            "name": "Soygaon",
            "marathi_name": "Soygaon"
        },
        {
            "id": "vil-nandgaon-takli-bk",
            "name": "Takli Bk",
            "marathi_name": "Takli Bk"
        },
        {
            "id": "vil-nandgaon-takli-kh",
            "name": "Takli Kh",
            "marathi_name": "Takli Kh"
        },
        {
            "id": "vil-nandgaon-talwade",
            "name": "Talwade",
            "marathi_name": "Talwade"
        },
        {
            "id": "vil-nandgaon-tandulwadi",
            "name": "Tandulwadi",
            "marathi_name": "Tandulwadi"
        },
        {
            "id": "vil-nandgaon-vasantnagar",
            "name": "Vasantnagar",
            "marathi_name": "Vasantnagar"
        },
        {
            "id": "vil-nandgaon-vehelgaon",
            "name": "Vehelgaon",
            "marathi_name": "Vehelgaon"
        },
        {
            "id": "vil-nandgaon-wadali-bk",
            "name": "Wadali Bk",
            "marathi_name": "Wadali Bk"
        },
        {
            "id": "vil-nandgaon-wadali-kh",
            "name": "Wadali Kh",
            "marathi_name": "Wadali Kh"
        },
        {
            "id": "vil-nandgaon-wakhari",
            "name": "Wakhari",
            "marathi_name": "Wakhari"
        },
        {
            "id": "vil-nandgaon-wanjarwadi",
            "name": "Wanjarwadi",
            "marathi_name": "Wanjarwadi"
        }
    ],
    "tal-chandwad": [
        {
            "id": "vil-chandwad-adgaon",
            "name": "Adgaon",
            "marathi_name": "Adgaon"
        },
        {
            "id": "vil-chandwad-ahirkhede",
            "name": "Ahirkhede",
            "marathi_name": "Ahirkhede"
        },
        {
            "id": "vil-chandwad-asarkhede",
            "name": "Asarkhede",
            "marathi_name": "Asarkhede"
        },
        {
            "id": "vil-chandwad-bahaduri",
            "name": "Bahaduri",
            "marathi_name": "Bahaduri"
        },
        {
            "id": "vil-chandwad-bhadane",
            "name": "Bhadane",
            "marathi_name": "Bhadane"
        },
        {
            "id": "vil-chandwad-bharvir",
            "name": "Bharvir",
            "marathi_name": "Bharvir"
        },
        {
            "id": "vil-chandwad-bhatgaon",
            "name": "Bhatgaon",
            "marathi_name": "Bhatgaon"
        },
        {
            "id": "vil-chandwad-bhayale",
            "name": "Bhayale",
            "marathi_name": "Bhayale"
        },
        {
            "id": "vil-chandwad-bhoyegaon",
            "name": "Bhoyegaon",
            "marathi_name": "Bhoyegaon"
        },
        {
            "id": "vil-chandwad-bhutyane",
            "name": "Bhutyane",
            "marathi_name": "Bhutyane"
        },
        {
            "id": "vil-chandwad-bopane",
            "name": "Bopane",
            "marathi_name": "Bopane"
        },
        {
            "id": "vil-chandwad-borale",
            "name": "Borale",
            "marathi_name": "Borale"
        },
        {
            "id": "vil-chandwad-chandvad-ct",
            "name": "Chandvad (CT)",
            "marathi_name": "Chandvad (CT)"
        },
        {
            "id": "vil-chandwad-chikhalambe",
            "name": "Chikhalambe",
            "marathi_name": "Chikhalambe"
        },
        {
            "id": "vil-chandwad-chinchole",
            "name": "Chinchole",
            "marathi_name": "Chinchole"
        },
        {
            "id": "vil-chandwad-dahegaon-manmad",
            "name": "Dahegaon Manmad",
            "marathi_name": "Dahegaon Manmad"
        },
        {
            "id": "vil-chandwad-dahiwad",
            "name": "Dahiwad",
            "marathi_name": "Dahiwad"
        },
        {
            "id": "vil-chandwad-dahyane",
            "name": "Dahyane",
            "marathi_name": "Dahyane"
        },
        {
            "id": "vil-chandwad-daregaon",
            "name": "Daregaon",
            "marathi_name": "Daregaon"
        },
        {
            "id": "vil-chandwad-deogaon",
            "name": "Deogaon",
            "marathi_name": "Deogaon"
        },
        {
            "id": "vil-chandwad-devergaon",
            "name": "Devergaon",
            "marathi_name": "Devergaon"
        },
        {
            "id": "vil-chandwad-dhodambe",
            "name": "Dhodambe",
            "marathi_name": "Dhodambe"
        },
        {
            "id": "vil-chandwad-dhondgavhan",
            "name": "Dhondgavhan",
            "marathi_name": "Dhondgavhan"
        },
        {
            "id": "vil-chandwad-dhotarkhede",
            "name": "Dhotarkhede",
            "marathi_name": "Dhotarkhede"
        },
        {
            "id": "vil-chandwad-dighwad",
            "name": "Dighwad",
            "marathi_name": "Dighwad"
        },
        {
            "id": "vil-chandwad-dongaon",
            "name": "Dongaon",
            "marathi_name": "Dongaon"
        },
        {
            "id": "vil-chandwad-dongargaon",
            "name": "Dongargaon",
            "marathi_name": "Dongargaon"
        },
        {
            "id": "vil-chandwad-dudhkhede",
            "name": "Dudhkhede",
            "marathi_name": "Dudhkhede"
        },
        {
            "id": "vil-chandwad-dugaon",
            "name": "Dugaon",
            "marathi_name": "Dugaon"
        },
        {
            "id": "vil-chandwad-ekrukhe",
            "name": "Ekrukhe",
            "marathi_name": "Ekrukhe"
        },
        {
            "id": "vil-chandwad-gangave",
            "name": "Gangave",
            "marathi_name": "Gangave"
        },
        {
            "id": "vil-chandwad-ganur",
            "name": "Ganur",
            "marathi_name": "Ganur"
        },
        {
            "id": "vil-chandwad-goharan",
            "name": "Goharan",
            "marathi_name": "Goharan"
        },
        {
            "id": "vil-chandwad-gurhale",
            "name": "Gurhale",
            "marathi_name": "Gurhale"
        },
        {
            "id": "vil-chandwad-harnul",
            "name": "Harnul",
            "marathi_name": "Harnul"
        },
        {
            "id": "vil-chandwad-harsul",
            "name": "Harsul",
            "marathi_name": "Harsul"
        },
        {
            "id": "vil-chandwad-hatti",
            "name": "Hatti",
            "marathi_name": "Hatti"
        },
        {
            "id": "vil-chandwad-hirapur",
            "name": "Hirapur",
            "marathi_name": "Hirapur"
        },
        {
            "id": "vil-chandwad-hivarkhede",
            "name": "Hivarkhede",
            "marathi_name": "Hivarkhede"
        },
        {
            "id": "vil-chandwad-indira-nagar",
            "name": "Indira Nagar",
            "marathi_name": "Indira Nagar"
        },
        {
            "id": "vil-chandwad-indraiwadi",
            "name": "Indraiwadi",
            "marathi_name": "Indraiwadi"
        },
        {
            "id": "vil-chandwad-jaitapur",
            "name": "Jaitapur",
            "marathi_name": "Jaitapur"
        },
        {
            "id": "vil-chandwad-jambutke",
            "name": "Jambutke",
            "marathi_name": "Jambutke"
        },
        {
            "id": "vil-chandwad-jopul",
            "name": "Jopul",
            "marathi_name": "Jopul"
        },
        {
            "id": "vil-chandwad-kalamdare",
            "name": "Kalamdare",
            "marathi_name": "Kalamdare"
        },
        {
            "id": "vil-chandwad-kalkhode",
            "name": "Kalkhode",
            "marathi_name": "Kalkhode"
        },
        {
            "id": "vil-chandwad-kanadgaon",
            "name": "Kanadgaon",
            "marathi_name": "Kanadgaon"
        },
        {
            "id": "vil-chandwad-kanmandale",
            "name": "Kanmandale",
            "marathi_name": "Kanmandale"
        },
        {
            "id": "vil-chandwad-katarwadi",
            "name": "Katarwadi",
            "marathi_name": "Katarwadi"
        },
        {
            "id": "vil-chandwad-kazisangvi",
            "name": "Kazisangvi",
            "marathi_name": "Kazisangvi"
        },
        {
            "id": "vil-chandwad-khadakjamb",
            "name": "Khadakjamb",
            "marathi_name": "Khadakjamb"
        },
        {
            "id": "vil-chandwad-khadakozar",
            "name": "Khadakozar",
            "marathi_name": "Khadakozar"
        },
        {
            "id": "vil-chandwad-kheldari",
            "name": "Kheldari",
            "marathi_name": "Kheldari"
        },
        {
            "id": "vil-chandwad-kokankhede",
            "name": "Kokankhede",
            "marathi_name": "Kokankhede"
        },
        {
            "id": "vil-chandwad-koltek",
            "name": "Koltek",
            "marathi_name": "Koltek"
        },
        {
            "id": "vil-chandwad-kundalgaon",
            "name": "Kundalgaon",
            "marathi_name": "Kundalgaon"
        },
        {
            "id": "vil-chandwad-kundane",
            "name": "Kundane",
            "marathi_name": "Kundane"
        },
        {
            "id": "vil-chandwad-malsane",
            "name": "Malsane",
            "marathi_name": "Malsane"
        },
        {
            "id": "vil-chandwad-mangrul",
            "name": "Mangrul",
            "marathi_name": "Mangrul"
        },
        {
            "id": "vil-chandwad-mesankhede-bk",
            "name": "Mesankhede Bk",
            "marathi_name": "Mesankhede Bk"
        },
        {
            "id": "vil-chandwad-mesankhede-kh",
            "name": "Mesankhede Kh",
            "marathi_name": "Mesankhede Kh"
        },
        {
            "id": "vil-chandwad-nandurtek",
            "name": "Nandurtek",
            "marathi_name": "Nandurtek"
        },
        {
            "id": "vil-chandwad-narayangaon",
            "name": "Narayangaon",
            "marathi_name": "Narayangaon"
        },
        {
            "id": "vil-chandwad-narayankhede",
            "name": "Narayankhede",
            "marathi_name": "Narayankhede"
        },
        {
            "id": "vil-chandwad-nawapur",
            "name": "Nawapur",
            "marathi_name": "Nawapur"
        },
        {
            "id": "vil-chandwad-nhanave",
            "name": "Nhanave",
            "marathi_name": "Nhanave"
        },
        {
            "id": "vil-chandwad-nimbale",
            "name": "Nimbale",
            "marathi_name": "Nimbale"
        },
        {
            "id": "vil-chandwad-nimgavhan",
            "name": "Nimgavhan",
            "marathi_name": "Nimgavhan"
        },
        {
            "id": "vil-chandwad-nimon",
            "name": "Nimon",
            "marathi_name": "Nimon"
        },
        {
            "id": "vil-chandwad-panhale",
            "name": "Panhale",
            "marathi_name": "Panhale"
        },
        {
            "id": "vil-chandwad-paregaon",
            "name": "Paregaon",
            "marathi_name": "Paregaon"
        },
        {
            "id": "vil-chandwad-parsul",
            "name": "Parsul",
            "marathi_name": "Parsul"
        },
        {
            "id": "vil-chandwad-pate",
            "name": "Pate",
            "marathi_name": "Pate"
        },
        {
            "id": "vil-chandwad-pathar-shembe",
            "name": "Pathar-shembe",
            "marathi_name": "Pathar-shembe"
        },
        {
            "id": "vil-chandwad-pimpalgaon-dhabli",
            "name": "Pimpalgaon-dhabli",
            "marathi_name": "Pimpalgaon-dhabli"
        },
        {
            "id": "vil-chandwad-pimpalnare",
            "name": "Pimpalnare",
            "marathi_name": "Pimpalnare"
        },
        {
            "id": "vil-chandwad-pimplad",
            "name": "Pimplad",
            "marathi_name": "Pimplad"
        },
        {
            "id": "vil-chandwad-puri",
            "name": "Puri",
            "marathi_name": "Puri"
        },
        {
            "id": "vil-chandwad-rahod",
            "name": "Rahod",
            "marathi_name": "Rahod"
        },
        {
            "id": "vil-chandwad-rajderwadi",
            "name": "Rajderwadi",
            "marathi_name": "Rajderwadi"
        },
        {
            "id": "vil-chandwad-rapali",
            "name": "Rapali",
            "marathi_name": "Rapali"
        },
        {
            "id": "vil-chandwad-raypur",
            "name": "Raypur",
            "marathi_name": "Raypur"
        },
        {
            "id": "vil-chandwad-redgaon-kh",
            "name": "Redgaon Kh",
            "marathi_name": "Redgaon Kh"
        },
        {
            "id": "vil-chandwad-salsane",
            "name": "Salsane",
            "marathi_name": "Salsane"
        },
        {
            "id": "vil-chandwad-shelu",
            "name": "Shelu",
            "marathi_name": "Shelu"
        },
        {
            "id": "vil-chandwad-sherisalaiban",
            "name": "Sherisalaiban",
            "marathi_name": "Sherisalaiban"
        },
        {
            "id": "vil-chandwad-shinde",
            "name": "Shinde",
            "marathi_name": "Shinde"
        },
        {
            "id": "vil-chandwad-shingve",
            "name": "Shingve",
            "marathi_name": "Shingve"
        },
        {
            "id": "vil-chandwad-shirsane",
            "name": "Shirsane",
            "marathi_name": "Shirsane"
        },
        {
            "id": "vil-chandwad-shirur",
            "name": "Shirur",
            "marathi_name": "Shirur"
        },
        {
            "id": "vil-chandwad-shivajinagar",
            "name": "Shivajinagar",
            "marathi_name": "Shivajinagar"
        },
        {
            "id": "vil-chandwad-shivare",
            "name": "Shivare",
            "marathi_name": "Shivare"
        },
        {
            "id": "vil-chandwad-sogras",
            "name": "Sogras",
            "marathi_name": "Sogras"
        },
        {
            "id": "vil-chandwad-soni-sangvi",
            "name": "Soni Sangvi",
            "marathi_name": "Soni Sangvi"
        },
        {
            "id": "vil-chandwad-sutarkhede",
            "name": "Sutarkhede",
            "marathi_name": "Sutarkhede"
        },
        {
            "id": "vil-chandwad-talegaon-rohi",
            "name": "Talegaon Rohi",
            "marathi_name": "Talegaon Rohi"
        },
        {
            "id": "vil-chandwad-talwade",
            "name": "Talwade",
            "marathi_name": "Talwade"
        },
        {
            "id": "vil-chandwad-tisgaon",
            "name": "Tisgaon",
            "marathi_name": "Tisgaon"
        },
        {
            "id": "vil-chandwad-urdhul",
            "name": "Urdhul",
            "marathi_name": "Urdhul"
        },
        {
            "id": "vil-chandwad-uswad",
            "name": "Uswad",
            "marathi_name": "Uswad"
        },
        {
            "id": "vil-chandwad-vad",
            "name": "Vad",
            "marathi_name": "Vad"
        },
        {
            "id": "vil-chandwad-vadalibhoi",
            "name": "Vadalibhoi",
            "marathi_name": "Vadalibhoi"
        },
        {
            "id": "vil-chandwad-vadbare",
            "name": "Vadbare",
            "marathi_name": "Vadbare"
        },
        {
            "id": "vil-chandwad-vadgaon-pangu",
            "name": "Vadgaon Pangu",
            "marathi_name": "Vadgaon Pangu"
        },
        {
            "id": "vil-chandwad-vadner-bhairao",
            "name": "Vadner Bhairao",
            "marathi_name": "Vadner Bhairao"
        },
        {
            "id": "vil-chandwad-vahegaonsal",
            "name": "Vahegaonsal",
            "marathi_name": "Vahegaonsal"
        },
        {
            "id": "vil-chandwad-vaki-bk",
            "name": "Vaki Bk",
            "marathi_name": "Vaki Bk"
        },
        {
            "id": "vil-chandwad-vaki-kh",
            "name": "Vaki Kh",
            "marathi_name": "Vaki Kh"
        },
        {
            "id": "vil-chandwad-varadi",
            "name": "Varadi",
            "marathi_name": "Varadi"
        },
        {
            "id": "vil-chandwad-vijaynagar",
            "name": "Vijaynagar",
            "marathi_name": "Vijaynagar"
        },
        {
            "id": "vil-chandwad-vitave",
            "name": "Vitave",
            "marathi_name": "Vitave"
        },
        {
            "id": "vil-chandwad-wagdardi",
            "name": "Wagdardi",
            "marathi_name": "Wagdardi"
        }
    ],
    "tal-niphad": [
        {
            "id": "vil-niphad-ahergaon",
            "name": "Ahergaon",
            "marathi_name": "Ahergaon"
        },
        {
            "id": "vil-niphad-amrut-nagar",
            "name": "Amrut Nagar",
            "marathi_name": "Amrut Nagar"
        },
        {
            "id": "vil-niphad-antarweli",
            "name": "Antarweli",
            "marathi_name": "Antarweli"
        },
        {
            "id": "vil-niphad-aurangpur",
            "name": "Aurangpur",
            "marathi_name": "Aurangpur"
        },
        {
            "id": "vil-niphad-banganganagar",
            "name": "Banganganagar",
            "marathi_name": "Banganganagar"
        },
        {
            "id": "vil-niphad-behed",
            "name": "Behed",
            "marathi_name": "Behed"
        },
        {
            "id": "vil-niphad-bharwas",
            "name": "Bharwas",
            "marathi_name": "Bharwas"
        },
        {
            "id": "vil-niphad-bhendali",
            "name": "Bhendali",
            "marathi_name": "Bhendali"
        },
        {
            "id": "vil-niphad-bhuse",
            "name": "Bhuse",
            "marathi_name": "Bhuse"
        },
        {
            "id": "vil-niphad-bokaddare",
            "name": "Bokaddare",
            "marathi_name": "Bokaddare"
        },
        {
            "id": "vil-niphad-bramhangaon-vanas",
            "name": "Bramhangaon Vanas",
            "marathi_name": "Bramhangaon Vanas"
        },
        {
            "id": "vil-niphad-bramhangaon-vinchur",
            "name": "Bramhangaon Vinchur",
            "marathi_name": "Bramhangaon Vinchur"
        },
        {
            "id": "vil-niphad-bramhanwade",
            "name": "Bramhanwade",
            "marathi_name": "Bramhanwade"
        },
        {
            "id": "vil-niphad-chandori",
            "name": "Chandori",
            "marathi_name": "Chandori"
        },
        {
            "id": "vil-niphad-chapadgaon",
            "name": "Chapadgaon",
            "marathi_name": "Chapadgaon"
        },
        {
            "id": "vil-niphad-chatori",
            "name": "Chatori",
            "marathi_name": "Chatori"
        },
        {
            "id": "vil-niphad-chehedi-kh",
            "name": "Chehedi Kh",
            "marathi_name": "Chehedi Kh"
        },
        {
            "id": "vil-niphad-chitegaon",
            "name": "Chitegaon",
            "marathi_name": "Chitegaon"
        },
        {
            "id": "vil-niphad-dahegaon",
            "name": "Dahegaon",
            "marathi_name": "Dahegaon"
        },
        {
            "id": "vil-niphad-darna-sangvi",
            "name": "Darna Sangvi",
            "marathi_name": "Darna Sangvi"
        },
        {
            "id": "vil-niphad-datyane",
            "name": "Datyane",
            "marathi_name": "Datyane"
        },
        {
            "id": "vil-niphad-davachwadi",
            "name": "Davachwadi",
            "marathi_name": "Davachwadi"
        },
        {
            "id": "vil-niphad-deogaon",
            "name": "Deogaon",
            "marathi_name": "Deogaon"
        },
        {
            "id": "vil-niphad-deopur",
            "name": "Deopur",
            "marathi_name": "Deopur"
        },
        {
            "id": "vil-niphad-dhanore",
            "name": "Dhanore",
            "marathi_name": "Dhanore"
        },
        {
            "id": "vil-niphad-dharangaon-khadak",
            "name": "Dharangaon Khadak",
            "marathi_name": "Dharangaon Khadak"
        },
        {
            "id": "vil-niphad-dharangaon-veer",
            "name": "Dharangaon Veer",
            "marathi_name": "Dharangaon Veer"
        },
        {
            "id": "vil-niphad-dindori",
            "name": "Dindori",
            "marathi_name": "Dindori"
        },
        {
            "id": "vil-niphad-dixi",
            "name": "Dixi",
            "marathi_name": "Dixi"
        },
        {
            "id": "vil-niphad-dongargaon",
            "name": "Dongargaon",
            "marathi_name": "Dongargaon"
        },
        {
            "id": "vil-niphad-gajarwadi",
            "name": "Gajarwadi",
            "marathi_name": "Gajarwadi"
        },
        {
            "id": "vil-niphad-gitakunj",
            "name": "Gitakunj",
            "marathi_name": "Gitakunj"
        },
        {
            "id": "vil-niphad-golegaon",
            "name": "Golegaon",
            "marathi_name": "Golegaon"
        },
        {
            "id": "vil-niphad-gondegaon-gondegaon-1",
            "name": "Gondegaon Gondegaon 1",
            "marathi_name": "Gondegaon Gondegaon 1"
        },
        {
            "id": "vil-niphad-gondegaon-2",
            "name": "Gondegaon 2",
            "marathi_name": "Gondegaon 2"
        },
        {
            "id": "vil-niphad-gorthan",
            "name": "Gorthan",
            "marathi_name": "Gorthan"
        },
        {
            "id": "vil-niphad-hanumannagar",
            "name": "Hanumannagar",
            "marathi_name": "Hanumannagar"
        },
        {
            "id": "vil-niphad-jalgaon",
            "name": "Jalgaon",
            "marathi_name": "Jalgaon"
        },
        {
            "id": "vil-niphad-jivhale",
            "name": "Jivhale",
            "marathi_name": "Jivhale"
        },
        {
            "id": "vil-niphad-kalgaon",
            "name": "Kalgaon",
            "marathi_name": "Kalgaon"
        },
        {
            "id": "vil-niphad-kanlad",
            "name": "Kanlad",
            "marathi_name": "Kanlad"
        },
        {
            "id": "vil-niphad-karanjgaon",
            "name": "Karanjgaon",
            "marathi_name": "Karanjgaon"
        },
        {
            "id": "vil-niphad-karanji-kh",
            "name": "Karanji Kh",
            "marathi_name": "Karanji Kh"
        },
        {
            "id": "vil-niphad-karsul",
            "name": "Karsul",
            "marathi_name": "Karsul"
        },
        {
            "id": "vil-niphad-kasabe-sukene",
            "name": "Kasabe Sukene",
            "marathi_name": "Kasabe Sukene"
        },
        {
            "id": "vil-niphad-kathargaon",
            "name": "Kathargaon",
            "marathi_name": "Kathargaon"
        },
        {
            "id": "vil-niphad-khadak-malegaon",
            "name": "Khadak Malegaon",
            "marathi_name": "Khadak Malegaon"
        },
        {
            "id": "vil-niphad-khangaon-najik",
            "name": "Khangaon Najik",
            "marathi_name": "Khangaon Najik"
        },
        {
            "id": "vil-niphad-khangaon-thadi",
            "name": "Khangaon Thadi",
            "marathi_name": "Khangaon Thadi"
        },
        {
            "id": "vil-niphad-khedale-zunge",
            "name": "Khedale Zunge",
            "marathi_name": "Khedale Zunge"
        },
        {
            "id": "vil-niphad-khede",
            "name": "Khede",
            "marathi_name": "Khede"
        },
        {
            "id": "vil-niphad-kokangaon",
            "name": "Kokangaon",
            "marathi_name": "Kokangaon"
        },
        {
            "id": "vil-niphad-kotamgaon",
            "name": "Kotamgaon",
            "marathi_name": "Kotamgaon"
        },
        {
            "id": "vil-niphad-kothure",
            "name": "Kothure",
            "marathi_name": "Kothure"
        },
        {
            "id": "vil-niphad-kumbhari",
            "name": "Kumbhari",
            "marathi_name": "Kumbhari"
        },
        {
            "id": "vil-niphad-kurudgaon",
            "name": "Kurudgaon",
            "marathi_name": "Kurudgaon"
        },
        {
            "id": "vil-niphad-lalpadi",
            "name": "Lalpadi",
            "marathi_name": "Lalpadi"
        },
        {
            "id": "vil-niphad-lasalgaon-ct",
            "name": "Lasalgaon (CT)",
            "marathi_name": "Lasalgaon (CT)"
        },
        {
            "id": "vil-niphad-lonwadi",
            "name": "Lonwadi",
            "marathi_name": "Lonwadi"
        },
        {
            "id": "vil-niphad-mahadevnagar",
            "name": "Mahadevnagar",
            "marathi_name": "Mahadevnagar"
        },
        {
            "id": "vil-niphad-mahajanpur",
            "name": "Mahajanpur",
            "marathi_name": "Mahajanpur"
        },
        {
            "id": "vil-niphad-majargaon",
            "name": "Majargaon",
            "marathi_name": "Majargaon"
        },
        {
            "id": "vil-niphad-manori-kh",
            "name": "Manori Kh",
            "marathi_name": "Manori Kh"
        },
        {
            "id": "vil-niphad-maralgoi-kh",
            "name": "Maralgoi Kh",
            "marathi_name": "Maralgoi Kh"
        },
        {
            "id": "vil-niphad-mauje-sukene",
            "name": "Mauje Sukene",
            "marathi_name": "Mauje Sukene"
        },
        {
            "id": "vil-niphad-mavalgoi-bk",
            "name": "Mavalgoi Bk",
            "marathi_name": "Mavalgoi Bk"
        },
        {
            "id": "vil-niphad-mhalsakore",
            "name": "Mhalsakore",
            "marathi_name": "Mhalsakore"
        },
        {
            "id": "vil-niphad-mukhed",
            "name": "Mukhed",
            "marathi_name": "Mukhed"
        },
        {
            "id": "vil-niphad-nagapur",
            "name": "Nagapur",
            "marathi_name": "Nagapur"
        },
        {
            "id": "vil-niphad-naitale",
            "name": "Naitale",
            "marathi_name": "Naitale"
        },
        {
            "id": "vil-niphad-nandgaon",
            "name": "Nandgaon",
            "marathi_name": "Nandgaon"
        },
        {
            "id": "vil-niphad-nandur-kh",
            "name": "Nandur Kh",
            "marathi_name": "Nandur Kh"
        },
        {
            "id": "vil-niphad-nandur-madhyameshwar",
            "name": "Nandur Madhyameshwar",
            "marathi_name": "Nandur Madhyameshwar"
        },
        {
            "id": "vil-niphad-nandurdi",
            "name": "Nandurdi",
            "marathi_name": "Nandurdi"
        },
        {
            "id": "vil-niphad-narayan-tembhi",
            "name": "Narayan Tembhi",
            "marathi_name": "Narayan Tembhi"
        },
        {
            "id": "vil-niphad-narayangaon",
            "name": "Narayangaon",
            "marathi_name": "Narayangaon"
        },
        {
            "id": "vil-niphad-nimgaon-wakada",
            "name": "Nimgaon Wakada",
            "marathi_name": "Nimgaon Wakada"
        },
        {
            "id": "vil-niphad-niphad",
            "name": "Niphad",
            "marathi_name": "Niphad"
        },
        {
            "id": "vil-niphad-oney",
            "name": "Oney",
            "marathi_name": "Oney"
        },
        {
            "id": "vil-niphad-ozar-ct",
            "name": "Ozar (CT)",
            "marathi_name": "Ozar (CT)"
        },
        {
            "id": "vil-niphad-pachore-bk",
            "name": "Pachore Bk",
            "marathi_name": "Pachore Bk"
        },
        {
            "id": "vil-niphad-pachore-kh",
            "name": "Pachore Kh",
            "marathi_name": "Pachore Kh"
        },
        {
            "id": "vil-niphad-pachorewani",
            "name": "Pachorewani",
            "marathi_name": "Pachorewani"
        },
        {
            "id": "vil-niphad-palkhed",
            "name": "Palkhed",
            "marathi_name": "Palkhed"
        },
        {
            "id": "vil-niphad-panchkeshwar",
            "name": "Panchkeshwar",
            "marathi_name": "Panchkeshwar"
        },
        {
            "id": "vil-niphad-pimpalas",
            "name": "Pimpalas",
            "marathi_name": "Pimpalas"
        },
        {
            "id": "vil-niphad-pimpalgaon-baswant",
            "name": "Pimpalgaon Baswant",
            "marathi_name": "Pimpalgaon Baswant"
        },
        {
            "id": "vil-niphad-pimpalgaon-najik-ct",
            "name": "Pimpalgaon Najik (CT)",
            "marathi_name": "Pimpalgaon Najik (CT)"
        },
        {
            "id": "vil-niphad-pimpalgaon-nipani",
            "name": "Pimpalgaon Nipani",
            "marathi_name": "Pimpalgaon Nipani"
        },
        {
            "id": "vil-niphad-pimpri",
            "name": "Pimpri",
            "marathi_name": "Pimpri"
        },
        {
            "id": "vil-niphad-ramnagar",
            "name": "Ramnagar",
            "marathi_name": "Ramnagar"
        },
        {
            "id": "vil-niphad-rampur",
            "name": "Rampur",
            "marathi_name": "Rampur"
        },
        {
            "id": "vil-niphad-ranwad",
            "name": "Ranwad",
            "marathi_name": "Ranwad"
        },
        {
            "id": "vil-niphad-rasalpur",
            "name": "Rasalpur",
            "marathi_name": "Rasalpur"
        },
        {
            "id": "vil-niphad-raulas",
            "name": "Raulas",
            "marathi_name": "Raulas"
        },
        {
            "id": "vil-niphad-redgaon",
            "name": "Redgaon",
            "marathi_name": "Redgaon"
        },
        {
            "id": "vil-niphad-rui",
            "name": "Rui",
            "marathi_name": "Rui"
        },
        {
            "id": "vil-niphad-saikhede",
            "name": "Saikhede",
            "marathi_name": "Saikhede"
        },
        {
            "id": "vil-niphad-sakore",
            "name": "Sakore",
            "marathi_name": "Sakore"
        },
        {
            "id": "vil-niphad-sarole-kh",
            "name": "Sarole Kh",
            "marathi_name": "Sarole Kh"
        },
        {
            "id": "vil-niphad-sarole-thadi",
            "name": "Sarole Thadi",
            "marathi_name": "Sarole Thadi"
        },
        {
            "id": "vil-niphad-sawali",
            "name": "Sawali",
            "marathi_name": "Sawali"
        },
        {
            "id": "vil-niphad-sawargaon",
            "name": "Sawargaon",
            "marathi_name": "Sawargaon"
        },
        {
            "id": "vil-niphad-shimpi-takali",
            "name": "Shimpi Takali",
            "marathi_name": "Shimpi Takali"
        },
        {
            "id": "vil-niphad-shingave",
            "name": "Shingave",
            "marathi_name": "Shingave"
        },
        {
            "id": "vil-niphad-shirasgaon",
            "name": "Shirasgaon",
            "marathi_name": "Shirasgaon"
        },
        {
            "id": "vil-niphad-shirwade-wakad",
            "name": "Shirwade Wakad",
            "marathi_name": "Shirwade Wakad"
        },
        {
            "id": "vil-niphad-shirwade-wani",
            "name": "Shirwade Wani",
            "marathi_name": "Shirwade Wani"
        },
        {
            "id": "vil-niphad-shivadi",
            "name": "Shivadi",
            "marathi_name": "Shivadi"
        },
        {
            "id": "vil-niphad-shivare",
            "name": "Shivare",
            "marathi_name": "Shivare"
        },
        {
            "id": "vil-niphad-shiwapur",
            "name": "Shiwapur",
            "marathi_name": "Shiwapur"
        },
        {
            "id": "vil-niphad-shriram-nagar",
            "name": "Shriram Nagar",
            "marathi_name": "Shriram Nagar"
        },
        {
            "id": "vil-niphad-shrirampur",
            "name": "Shrirampur",
            "marathi_name": "Shrirampur"
        },
        {
            "id": "vil-niphad-sonewadi-bk",
            "name": "Sonewadi Bk",
            "marathi_name": "Sonewadi Bk"
        },
        {
            "id": "vil-niphad-sonewadi-kh",
            "name": "Sonewadi Kh",
            "marathi_name": "Sonewadi Kh"
        },
        {
            "id": "vil-niphad-songaon",
            "name": "Songaon",
            "marathi_name": "Songaon"
        },
        {
            "id": "vil-niphad-subhash-nagar",
            "name": "Subhash Nagar",
            "marathi_name": "Subhash Nagar"
        },
        {
            "id": "vil-niphad-sundarpur",
            "name": "Sundarpur",
            "marathi_name": "Sundarpur"
        },
        {
            "id": "vil-niphad-takali-vinchur",
            "name": "Takali Vinchur",
            "marathi_name": "Takali Vinchur"
        },
        {
            "id": "vil-niphad-talwade",
            "name": "Talwade",
            "marathi_name": "Talwade"
        },
        {
            "id": "vil-niphad-tamaswadi",
            "name": "Tamaswadi",
            "marathi_name": "Tamaswadi"
        },
        {
            "id": "vil-niphad-tarukhedle",
            "name": "Tarukhedle",
            "marathi_name": "Tarukhedle"
        },
        {
            "id": "vil-niphad-thergaon",
            "name": "Thergaon",
            "marathi_name": "Thergaon"
        },
        {
            "id": "vil-niphad-thetale",
            "name": "Thetale",
            "marathi_name": "Thetale"
        },
        {
            "id": "vil-niphad-ugaon",
            "name": "Ugaon",
            "marathi_name": "Ugaon"
        },
        {
            "id": "vil-niphad-umbarkhed",
            "name": "Umbarkhed",
            "marathi_name": "Umbarkhed"
        },
        {
            "id": "vil-niphad-vadali-najik",
            "name": "Vadali Najik",
            "marathi_name": "Vadali Najik"
        },
        {
            "id": "vil-niphad-vanasgaon",
            "name": "Vanasgaon",
            "marathi_name": "Vanasgaon"
        },
        {
            "id": "vil-niphad-varhe-davna",
            "name": "Varhe Davna",
            "marathi_name": "Varhe Davna"
        },
        {
            "id": "vil-niphad-vijay-nagar",
            "name": "Vijay Nagar",
            "marathi_name": "Vijay Nagar"
        },
        {
            "id": "vil-niphad-vinchur",
            "name": "Vinchur",
            "marathi_name": "Vinchur"
        },
        {
            "id": "vil-niphad-vishnu-nagar",
            "name": "Vishnu Nagar",
            "marathi_name": "Vishnu Nagar"
        },
        {
            "id": "vil-niphad-vitthalwadi",
            "name": "Vitthalwadi",
            "marathi_name": "Vitthalwadi"
        },
        {
            "id": "vil-niphad-wahegaon",
            "name": "Wahegaon",
            "marathi_name": "Wahegaon"
        },
        {
            "id": "vil-niphad-wakad",
            "name": "Wakad",
            "marathi_name": "Wakad"
        },
        {
            "id": "vil-niphad-wavi",
            "name": "Wavi",
            "marathi_name": "Wavi"
        },
        {
            "id": "vil-niphad-welapur",
            "name": "Welapur",
            "marathi_name": "Welapur"
        }
    ]
}

import os
import json

_JALNA_VILLAGES_PATH = os.path.join(os.path.dirname(__file__), "jalna_villages.json")
if os.path.exists(_JALNA_VILLAGES_PATH):
    try:
        with open(_JALNA_VILLAGES_PATH, "r", encoding="utf-8") as _f:
            _jalna_data = json.load(_f)
            VILLAGES.update(_jalna_data)
    except Exception as _e:
        print("Failed to load jalna_villages.json:", _e)

_PUNE_VILLAGES_PATH = os.path.join(os.path.dirname(__file__), "pune_villages.json")
if os.path.exists(_PUNE_VILLAGES_PATH):
    try:
        with open(_PUNE_VILLAGES_PATH, "r", encoding="utf-8") as _f:
            _pune_data = json.load(_f)
            VILLAGES.update(_pune_data)
    except Exception as _e:
        print("Failed to load pune_villages.json:", _e)

MANDI_PRICES = [
    {
        "mandi_name": "Malegaon APMC",
        "district": "Nashik",
        "taluka": "Malegaon",
        "crop_name": "Onion (कांदा)",
        "crop_key": "ONION",
        "crop_variety": "Red Onion (लाल कांदा)",
        "min_price": 1800,
        "modal_price": 2400,
        "max_price": 2650,
        "formatted_min_price": "₹1,800",
        "formatted_modal_price": "₹2,400",
        "formatted_max_price": "₹2,650",
        "price_change": "+₹60 (▲ 2.5%)",
        "daily_arrivals_quintals": 14500,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.8% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources (Agmarknet, MSAMB & Local APMC Auction)",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Lasalgaon APMC",
        "district": "Nashik",
        "taluka": "Niphad",
        "crop_name": "Onion (कांदा)",
        "crop_key": "ONION",
        "crop_variety": "Summer Onion (उन्हाळ कांदा)",
        "min_price": 2100,
        "modal_price": 2650,
        "max_price": 2900,
        "formatted_min_price": "₹2,100",
        "formatted_modal_price": "₹2,650",
        "formatted_max_price": "₹2,900",
        "price_change": "+₹80 (▲ 3.1%)",
        "daily_arrivals_quintals": 32400,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.9% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "Lasalgaon APMC Direct"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources (Agmarknet, MSAMB & Local APMC Auction)",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Pimplegaon APMC",
        "district": "Nashik",
        "taluka": "Niphad",
        "crop_name": "Onion (कांदा)",
        "crop_key": "ONION",
        "crop_variety": "Red Onion (लाल कांदा)",
        "min_price": 1950,
        "modal_price": 2500,
        "max_price": 2780,
        "formatted_min_price": "₹1,950",
        "formatted_modal_price": "₹2,500",
        "formatted_max_price": "₹2,780",
        "price_change": "+₹45 (▲ 1.8%)",
        "daily_arrivals_quintals": 21800,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.7% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Pimplegaon APMC",
        "district": "Nashik",
        "taluka": "Niphad",
        "crop_name": "Grapes (द्राक्षे)",
        "crop_key": "GRAPES",
        "crop_variety": "Thompson Seedless (निर्यातक्षम)",
        "min_price": 6500,
        "modal_price": 8500,
        "max_price": 10500,
        "formatted_min_price": "₹6,500",
        "formatted_modal_price": "₹8,500",
        "formatted_max_price": "₹10,500",
        "price_change": "+₹150 (▲ 1.8%)",
        "daily_arrivals_quintals": 4200,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.8% Live",
        "verification_sources": [
            "GrapeNet Direct Feed",
            "MSAMB Gateway",
            "APMC Export Auction"
        ],
        "cross_check_status": "Verified via GrapeNet & APMC Direct Auction",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Chandwad APMC",
        "district": "Nashik",
        "taluka": "Chandwad",
        "crop_name": "Onion (कांदा)",
        "crop_key": "ONION",
        "crop_variety": "Red Onion (लाल कांदा)",
        "min_price": 1750,
        "modal_price": 2350,
        "max_price": 2600,
        "formatted_min_price": "₹1,750",
        "formatted_modal_price": "₹2,350",
        "formatted_max_price": "₹2,600",
        "price_change": "+₹30 (▲ 1.3%)",
        "daily_arrivals_quintals": 11200,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.6% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Nandgaon APMC",
        "district": "Nashik",
        "taluka": "Nandgaon",
        "crop_name": "Maize (मका)",
        "crop_key": "MAIZE",
        "crop_variety": "Yellow Hybrid Maize (पिवळी मका)",
        "min_price": 1950,
        "modal_price": 2250,
        "max_price": 2450,
        "formatted_min_price": "₹1,950",
        "formatted_modal_price": "₹2,250",
        "formatted_max_price": "₹2,450",
        "price_change": "₹0 (Stable)",
        "daily_arrivals_quintals": 8900,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.5% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "stable",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Niphad APMC",
        "district": "Nashik",
        "taluka": "Niphad",
        "crop_name": "Wheat (गहू)",
        "crop_key": "WHEAT",
        "crop_variety": "Lokwan Wheat (लोकवण गहू)",
        "min_price": 2350,
        "modal_price": 2700,
        "max_price": 2920,
        "formatted_min_price": "₹2,350",
        "formatted_modal_price": "₹2,700",
        "formatted_max_price": "₹2,920",
        "price_change": "+₹20 (▲ 0.7%)",
        "daily_arrivals_quintals": 6400,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.7% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Latur APMC",
        "district": "Latur",
        "taluka": "Latur",
        "crop_name": "Soyabean (सोयाबीन)",
        "crop_key": "SOYABEAN",
        "crop_variety": "Yellow Soyabean (पिवळे सोयाबीन)",
        "min_price": 4350,
        "modal_price": 4650,
        "max_price": 4890,
        "formatted_min_price": "₹4,350",
        "formatted_modal_price": "₹4,650",
        "formatted_max_price": "₹4,890",
        "price_change": "₹0 (Stable)",
        "daily_arrivals_quintals": 18500,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.9% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "Latur APMC Direct"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "stable",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Jalna APMC",
        "district": "Jalna",
        "taluka": "Jalna",
        "crop_name": "Cotton (कापूस)",
        "crop_key": "COTTON",
        "crop_variety": "Medium Staple Cotton (मध्यम लांब धागा)",
        "min_price": 6800,
        "modal_price": 7250,
        "max_price": 7550,
        "formatted_min_price": "₹6,800",
        "formatted_modal_price": "₹7,250",
        "formatted_max_price": "₹7,550",
        "price_change": "+₹120 (▲ 1.7%)",
        "daily_arrivals_quintals": 9200,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.8% Live",
        "verification_sources": [
            "Cotton Corporation of India",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Verified via CCI & APMC Direct Auction",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Solapur APMC",
        "district": "Solapur",
        "taluka": "Solapur North",
        "crop_name": "Pomegranate (डाळिंब)",
        "crop_key": "POMEGRANATE",
        "crop_variety": "Bhagwa Pomegranate (भगवा डाळिंब)",
        "min_price": 4500,
        "modal_price": 6200,
        "max_price": 7800,
        "formatted_min_price": "₹4,500",
        "formatted_modal_price": "₹6,200",
        "formatted_max_price": "₹7,800",
        "price_change": "+₹100 (▲ 1.6%)",
        "daily_arrivals_quintals": 5600,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.7% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "up",
        "last_updated": "14 Aug 2026"
    },
    {
        "mandi_name": "Pune APMC",
        "district": "Pune",
        "taluka": "Haveli",
        "crop_name": "Gram (हरभरा)",
        "crop_key": "GRAM",
        "crop_variety": "Vijay Chana (विजय हरभरा)",
        "min_price": 5200,
        "modal_price": 5800,
        "max_price": 6400,
        "formatted_min_price": "₹5,200",
        "formatted_modal_price": "₹5,800",
        "formatted_max_price": "₹6,400",
        "price_change": "-₹30 (▼ 0.5%)",
        "daily_arrivals_quintals": 7800,
        "unit": "Quintal",
        "verification_badge": "✅ 3-SOURCE VERIFIED",
        "confidence_score": "99.6% Live",
        "verification_sources": [
            "Agmarknet Direct Feed",
            "MSAMB Gateway",
            "APMC Direct Auction"
        ],
        "cross_check_status": "Cross-Checked across 3 Sources",
        "trend": "down",
        "last_updated": "14 Aug 2026"
    }
]

HELPLINES = [
    {
        "id": "help-1",
        "title": "Kisan Call Center (किसान कॉल सेंटर)",
        "number": "1800-180-1551",
        "description": "Toll-free 24x7 expert agricultural advice in Marathi & Hindi"
    },
    {
        "id": "help-2",
        "title": "MahaAgri Farmer Helpline (महाराष्ट्र कृषी विभाग)",
        "number": "1800-233-0444",
        "description": "Government crop insurance, PM-Kisan & subsidy assistance"
    },
    {
        "id": "help-3",
        "title": "MSAMB Mandi Price Enquiry (बाजार समिती)",
        "number": "020-24268297",
        "description": "Maharashtra State Agricultural Marketing Board market rate helpdesk"
    }
]

NEWS_ITEMS = [
    {
        "id": "news-1",
        "title": "Central Govt Cuts Onion Export Duty from 40% to 20% & Lifts Minimum Export Price (MEP)",
        "title_marathi": "केंद्र सरकारतर्फे कांदा निर्यातीवरील शुल्क ४०% वरून २०% पर्यंत कमी; किमान निर्यात मूल्य (MEP) रद्द",
        "category": "EXPORT_IMPORT",
        "category_label": "🚢 EXPORT & IMPORT (निर्यात-आयात)",
        "impact_tag": "BULLISH (+ भाव वाढ)",
        "impact_color": "emerald",
        "date": "05 Oct 2026",
        "timestamp": "Just Now (ताज्या घडामोडी)",
        "summary": "The central government has officially slashed export duty on onions from 40% to 20% and lifted MEP restrictions to encourage outbound shipments before Diwali.",
        "summary_marathi": "दिवाळीच्या पार्श्वभूमीवर कांदा उत्पादकांना मोठा दिलासा! केंद्र सरकारने कांदा निर्यातीवरील शुल्क ४०% वरून २०% केले असून ५५० डॉलर प्रति टनची किमान निर्यात मूल्य अट पूर्णपणे रद्द केली आहे. यामुळे आखाती देशात व बांगलादेशात निर्यात वाढेल.",
        "source": "DGFT & Ministry of Commerce",
        "crops_affected": ["Onion (कांदा)"],
        "full_report": "केंद्रीय वाणिज्य व उद्योग मंत्रालयाने जारी केलेल्या अधिसूचनेनुसार कांदा निर्यातीवरील शुल्क ४० टक्क्यांवरून २० टक्के करण्यात आले आहे. तसेच किमान निर्यात मूल्य (MEP) पूर्णपणे काढून टाकण्यात आले आहे.\n\nबाजार परिणाम:\n• लासलगाव, पिंपळगाव, मालेगाव व उमराणे बाजारात कांद्याच्या सरासरी भावात क्विंटलमागे ₹३०० ते ₹५०० ची वाढ अपेक्षित आहे.\n• बांगलादेश, मलेशिया, दुबई व श्रीलंका या पारंपरिक बाजारपेठांमध्ये महाराष्ट्रातील लाल व उन्हाळ कांद्याला मोठी मागणी निर्माण होईल.\n\nशेतकऱ्यांना सल्ला:\nचांगल्या गुणवत्तेचा वाळलेला कांदा प्रतवारी करून बाजारात टप्प्याटप्प्याने विकावा, घाईगडबडीत ओला कांदा बाजारात आणू नये."
    },
    {
        "id": "news-2",
        "title": "Lasalgaon & Pimplegaon APMC Onion Prices Jump to ₹2,650/Qtl Ahead of Festive Demand",
        "title_marathi": "लासलगाव व पिंपळगाव बाजारात कांद्याचे सरासरी भाव ₹२,६५० प्रति क्विंटलवर; आवक ३२,००० क्विंटल",
        "category": "MANDI_PRICES",
        "category_label": "🧅 MANDI PRICES (बाजार भाव)",
        "impact_tag": "PRICE SURGE (भाव तेजी)",
        "impact_color": "emerald",
        "date": "05 Oct 2026",
        "timestamp": "1 Hour Ago",
        "summary": "Festival demand across North and South India pushed onion modal prices to ₹2,650/quintal in Asia's largest onion market at Lasalgaon.",
        "summary_marathi": "उत्तर व दक्षिण भारतातून वाढलेल्या मागणीमुळे आशियातील सर्वात मोठ्या लासलगाव कृषी उत्पन्न बाजार समितीत उन्हाळ कांद्याचे सर्वसाधारण दर ₹२,६५० वर पोहोचले असून कमाल भाव ₹२,९०० प्रति क्विंटल नोंदवले गेले आहेत.",
        "source": "Lasalgaon APMC Market Bulletin",
        "crops_affected": ["Onion (कांदा)"],
        "full_report": "लासलगाव आणि पिंपळगाव बसवंत बाजार समितीत आज कांद्याचे लिलाव तेजीत पार पडले. एकूण ३२,४०० क्विंटल कांद्याची आवक नोंदवली गेली.\n\nलिलाव तपशील:\n• किमान भाव: ₹२,१०० /क्विंटल\n• सर्वसाधारण भाव: ₹२,६५० /क्विंटल\n• कमाल भाव: ₹२,९०० /क्विंटल\n\nबाजार कल: दिल्ली, कोलकाता, बंगळुरू व चेन्नई येथील व्यापारी खरेदीसाठी सक्रिय आहेत. पुढील आठवड्यातही मागणी मजबूत राहण्याची शक्यता वर्तवण्यात आली आहे."
    },
    {
        "id": "news-3",
        "title": "NAFED Opens 240 MSP Procurement Centers for Maize (₹2,225/Qtl) & Cotton (₹7,521/Qtl)",
        "title_marathi": "नाफेड व सीसीआयकडून मका (₹२,२२५) आणि कापूस (₹७,५२१) हमीभाव खरेदी केंद्र सुरू",
        "category": "GOVT_SCHEMES",
        "category_label": "🏛️ GOVT SCHEME & MSP (शासकीय योजना व हमीभाव)",
        "impact_tag": "MSP GUARANTEE (हमीभाव हमी)",
        "impact_color": "blue",
        "date": "04 Oct 2026",
        "timestamp": "Today",
        "summary": "NAFED and Cotton Corporation of India (CCI) set up 240 government procurement counters across Maharashtra to purchase kharif crops at Minimum Support Prices.",
        "summary_marathi": "महाराष्ट्रभरातील मका व कापूस उत्पादक शेतकऱ्यांना हमीभाव मिळावा यासाठी नाफेड आणि कॉटन कॉर्पोरेशन ऑफ इंडियाने २४० अधिकृत खरेदी केंद्रे सुरू केली आहेत. मक्यासाठी ₹२,२२५ व मध्यम धाग्याच्या कापसासाठी ₹७,५२१ हमीभाव दिला जात आहे.",
        "source": "NAFED & Maharashtra State Co-op Marketing Fed",
        "crops_affected": ["Maize (मका)", "Cotton (कापूस)"],
        "full_report": "खरिपातील मका व कापूस काढणीला वेग आला असताना खुल्या बाजारात भाव पडू नयेत म्हणून शासनाने हमीभाव खरेदी केंद्रे कार्यान्वित केली आहेत.\n\nमहत्त्वाचे तपशील:\n• मका हमीभाव: ₹२,२२५ /क्विंटल\n• कापूस हमीभाव: ₹७,५२१ /क्विंटल (मध्यम धागा) व ₹८,०८० /क्विंटल (लांब धागा)\n• नोंदणी: शेतकऱ्यांनी ७/१२ उतारा, आधार कार्ड व बँक पासबुकसह स्थानिक खरेदी केंद्रावर किंवा महाडीबीटी पोर्टलवर ऑनलाइन शेतकरी नोंदणी करावी.\n• चुकारे थेट आधार लिंक बँक खात्यात १० ते १२ दिवसांत जमा केले जातील."
    },
    {
        "id": "news-4",
        "title": "Latur & Jalna APMC: New Crop Soybean Prices Firm at ₹4,750/Qtl Amid Heavy Oil Mill Buying",
        "title_marathi": "लातूर व जालना बाजारात नवीन सोयाबीनचे भाव ₹४,७५० वर स्थिर; तेल गिरण्यांकडून जोरदार खरेदी",
        "category": "MANDI_PRICES",
        "category_label": "🧅 MANDI PRICES (बाजार भाव)",
        "impact_tag": "DEMAND STEADY (स्थिर मागणी)",
        "impact_color": "blue",
        "date": "04 Oct 2026",
        "timestamp": "Yesterday",
        "summary": "High domestic demand for soyoil and export demand for de-oiled cake (DOC) has supported soybean prices above the ₹4,650 support level in Marathwada.",
        "summary_marathi": "खाद्यतेलाची वाढती मागणी आणि डि-ऑइल केक (पेंड) निर्यातीतील तेजीमुळे मराठवाड्यातील मुख्य बाजारपेठ लातूर व जालना येथे पिवळ्या सोयाबीनचे भाव ₹४,३५० ते ₹४,८९० दरम्यान व्यवहार करत असून सरासरी दर ₹४,६५० ते ₹४,७५० आहेत.",
        "source": "SOPA (Soybean Processors Association)",
        "crops_affected": ["Soybean (सोयाबीन)"],
        "full_report": "मराठवाडा व विदर्भात नवीन सोयाबीनची आवक सुरू झाली असून आवकेत आर्द्रतेचे प्रमाण १२% च्या आत असणाऱ्या दर्जेदार मालाला व्यापारी चढ्या दराने खरेदी करत आहेत.\n\nसल्ला: सोयाबीन काढणीनंतर शेतात किंवा खळ्यात व्यवस्थित वाळवून १२% पेक्षा कमी ओलावा असतानाच विक्रीस आणावे, जेणेकरून चांगला भाव मिळेल."
    },
    {
        "id": "news-5",
        "title": "IMD Weather Advisory: Moderate Showers Forecast for Nashik, Marathwada; Spraying Caution",
        "title_marathi": "हवामान विभागाचा इशारा: नाशिक, पुणे व मराठवाड्यात विजांसह पावसाची शक्यता; औषध फवारणी थांबवा",
        "category": "WEATHER_ALERTS",
        "category_label": "⛈️ WEATHER ALERT (हवामान अंदाज)",
        "impact_tag": "CAUTION (सावधगिरी बाळगा)",
        "impact_color": "amber",
        "date": "05 Oct 2026",
        "timestamp": "4 Hours Ago",
        "summary": "IMD Pune issues a weather caution advising farmers in North Maharashtra and Marathwada to suspend pesticide sprays and keep harvested produce in covered sheds.",
        "summary_marathi": "प्रादेशिक हवामान केंद्र, पुणे यांनी पुढील ४८ तासांत नाशिक, अहमदनगर, पुणे आणि मराठवाड्यातील काही भागांत विजांच्या कडकडाटासह हलक्या ते मध्यम स्वरूपाच्या पावसाचा अंदाज वर्तवला आहे. यामुळे द्राक्ष, भाजीपाला व कांदा पिकांवर फवारणी पुढे ढकलावी.",
        "source": "IMD Pune Meteorological Centre",
        "crops_affected": ["Grapes (द्राक्षे)", "Onion (कांदा)", "Tomato (टोमॅटो)"],
        "full_report": "हवामान खात्याच्या अंदाजानुसार पुढील २ दिवस दुपारनंतर ढगाळ वातावरण व स्थानिक वादळी पाऊस पडण्याची दाट शक्यता आहे.\n\nकृषी विद्यापीठाचा सल्ला:\n१. पुढील ४८ तास कोणतीही रासायनिक कीटकनाशक किंवा बुरशीनाशक फवारणी करू नये. फवारलेले औषध पावसात वाहून जाऊन नुकसान होईल.\n२. शेतातून पाणी वाहून जाण्यासाठी चर तयार ठेवावेत.\n३. काढलेला कांदा, मका व भाजीपाला शेतात उघड्यावर न ठेवता सुरक्षित शेड किंवा ताडपत्रीखाली झाकून ठेवावा."
    },
    {
        "id": "news-6",
        "title": "Namo Shetkari Mahasanman Nidhi: 4th Installment of ₹2,000 Transferred to 90 Lakh Farmers",
        "title_marathi": "नमो शेतकरी महासन्मान निधी: ९० लाख शेतकऱ्यांच्या बँक खात्यात प्रत्येकी ₹२,००० थेट जमा",
        "category": "GOVT_SCHEMES",
        "category_label": "🏛️ GOVT SCHEME (शासकीय योजना)",
        "impact_tag": "FUNDS DISBURSED (अनुदान जमा)",
        "impact_color": "emerald",
        "date": "03 Oct 2026",
        "timestamp": "2 Days Ago",
        "summary": "Maharashtra State Government successfully credited the 4th instalment of the Namo Shetkari Mahasanman Nidhi scheme via DBT directly into eligible farmers' Aadhaar-linked accounts.",
        "summary_marathi": "महाराष्ट्र शासनाने नमो शेतकरी महासन्मान निधी योजनेचा चौथा हप्ता डीबीटीद्वारे राज्यातील पात्र ९० लाख शेतकरी कुटुंबांच्या बँक खात्यात प्रत्येकी ₹२,००० प्रमाणे ₹१,८०० कोटींपेक्षा अधिक निधी थेट जमा केला आहे.",
        "source": "Maharashtra Dept of Agriculture & DBT Portal",
        "crops_affected": ["All Crops (सर्व पिके)"],
        "full_report": "नमो शेतकरी महासन्मान निधी योजनेच्या लाभार्थ्यांना पीएम-किसान योजनेच्या ₹६,००० शिवाय राज्य शासनाकडून दरवर्षी अतिरिक्त ₹६,००० (३ हप्त्यांमध्ये प्रत्येकी ₹२,०००) दिले जातात.\n\nशेतकऱ्यांनी आपले बँक खाते व आधार प्रमाणीकरण (e-KYC) पूर्ण झाले आहे की नाही हे तपासण्यासाठी नमो शेतकरी अधिकृत पोर्टल किंवा महाडीबीटी संकेतस्थळावर तपासावे."
    },
    {
        "id": "news-7",
        "title": "Solapur & Indapur Bhagwa Pomegranate Export Shipments Fetch Record ₹10,500/Qtl",
        "title_marathi": "सोलापूर व इंदापूरच्या भगवा डाळिंबाला निर्यातीत उच्चांकी ₹१०,५०० प्रति क्विंटल दर",
        "category": "EXPORT_IMPORT",
        "category_label": "🚢 EXPORT & IMPORT (निर्यात-आयात)",
        "impact_tag": "RECORD HIGH (उच्चांकी दर)",
        "impact_color": "purple",
        "date": "02 Oct 2026",
        "timestamp": "3 Days Ago",
        "summary": "Heavy export demand from Europe and the Gulf for export-grade Bhagwa pomegranates has rewarded growers in Solapur, Pune, and Ahmednagar districts.",
        "summary_marathi": "युरोपीय युनियन व आखाती देशांमध्ये महाराष्ट्रातील भगवा डाळिंबाला वाढत्या मागणीमुळे सोलापूर व बारामती भागातील रेसिड्यू-फ्री (अवशेषमुक्त) डाळिंबाला ₹८,५०० ते ₹१०,५०० प्रति क्विंटल इतका विक्रमी दर मिळत आहे.",
        "source": "APEDA & MahaPomegranate Board",
        "crops_affected": ["Pomegranate (डाळिंब)"],
        "full_report": "अपेडा (APEDA) आणि महाराष्ट्र राज्य डाळिंब उत्पादक संघामार्फत युरोप व मध्यपूर्वेसाठी निर्यात कंटेनर्स रवाना होत आहेत.\n\nडाळिंब उत्पादकांना शिफारस:\n• डागविरहित आणि लाल गर्द दाण्यांच्या 'ए' ग्रेड फळांची काढणी योग्य वेळी करावी.\n• पॅकहौसींग व कोल्ड स्टोरेज सुविधांचा लाभ घेऊन थेट निर्यातदारांशी करार केल्यास शेतकऱ्यांना चांगला नफा मिळतो."
    },
    {
        "id": "news-8",
        "title": "Central Govt Approves Duty-Free Soybean Oil Imports Quota Expiry; Domestic Farmers Rejoice",
        "title_marathi": "कच्च्या खाद्यतेलाच्या आयात शुल्कात वाढ; देशांतर्गत सोयाबीन व सूर्यफूल उत्पादक शेतकऱ्यांना दिलासा",
        "category": "MANDI_PRICES",
        "category_label": "🧅 MANDI PRICES & POLICY (बाजार भाव धोरण)",
        "impact_tag": "POLICY BOOST (धोरणात्मक लाभ)",
        "impact_color": "emerald",
        "date": "01 Oct 2026",
        "timestamp": "4 Days Ago",
        "summary": "To protect domestic oilseed farmers during the harvest season, the government raised custom duties on crude palm and soybean oils.",
        "summary_marathi": "स्थानिक तेलबिया उत्पादकांना हमीभावापेक्षा जास्त दर मिळावेत यासाठी केंद्र सरकारने आयात केल्या जाणाऱ्या खाद्यतेलावर आयात शुल्क वाढवले आहे. यामुळे देशी सोयाबीनच्या भावाला मोठा आधार मिळाला आहे.",
        "source": "Ministry of Finance & SEA (Solvent Extractors)",
        "crops_affected": ["Soybean (सोयाबीन)"],
        "full_report": "खरिपातील सोयाबीन काढणी सुरू होत असताना आयात तेलावर २०% शुल्क लागू केल्याने स्थानिक तेल मिलधारकांकडून देशी सोयाबीनची मागणी प्रचंड वाढली आहे. यामुळे आगामी हंगामात सोयाबीन भाव हमीभावाच्या (₹४,८९२) वर राहण्याचा अंदाज आहे."
    }
]


GOVT_SCHEMES = [
    {
        "id": "scheme-1",
        "title": "नमो शेतकरी महासन्मान निधी योजना (Namo Shetkari Mahasanman Nidhi)",
        "category": "STATE_SUBSIDY",
        "category_title": "राज्य शासन अनुदान",
        "benefit_amount": "₹6,000 प्रति वर्ष (₹2,000 x 3 हप्ते)",
        "eligibility": "महाराष्ट्रातील सर्व पीएम-किसान पात्र जमीनधारक शेतकरी.",
        "description": "केंद्र शासनाच्या PM-Kisan योजनेच्या धर्तीवर महाराष्ट्र शासनाकडून अतिरिक्त ₹६,००० वार्षिक आर्थिक मदत थेट बँक खात्यात.",
        "portal_url": "https://nsmny.mahait.org",
        "portal_name": "Namo Shetkari Official Portal",
        "badge": "🏛️ महाराष्ट्र शासन"
    },
    {
        "id": "scheme-2",
        "title": "मुख्यमंत्री सौर कृषी पंप योजना / PM-KUSUM (Solar Agri Pump Yojana)",
        "category": "SOLAR_IRRIGATION",
        "category_title": "सौर व सिंचन योजना",
        "benefit_amount": "९०% ते ९५% शासकीय अनुदान (3 HP, 5 HP, 7.5 HP)",
        "eligibility": "शेतात पाण्याची उपलब्धता असणारे व महावितरणचे वीज कनेक्शन नसलेले शेतकरी.",
        "description": "दिवसा हक्काची वीज मिळण्यासाठी सौर कृषी पंप संचावर ९०% पेक्षा जास्त सबसिडी. महावितरण/महाडीबीटी द्वारे अर्ज करावा.",
        "portal_url": "https://www.mahadiscom.in/solar",
        "portal_name": "MahaDiscom Solar Portal",
        "badge": "☀️ महाऊर्जा / PM-KUSUM"
    },
    {
        "id": "scheme-3",
        "title": "मागेल त्याला विहीर / सिंचन विहीर योजना (Magel Tyala Vihir Scheme)",
        "category": "SOLAR_IRRIGATION",
        "category_title": "सौर व सिंचन योजना",
        "benefit_amount": "₹४.०० लाख रुपये नवीन सिंचन विहिरीसाठी अनुदान",
        "eligibility": "किमान ०.४० हेक्टर शेतजमीन असणारे लहान व अल्पभूधारक शेतकरी.",
        "description": "शेतात शाश्वत पाणी उपलब्ध होण्यासाठी ४ लाख रुपयांपर्यंत शासकीय अनुदान. मनरेगा व कृषी विभागामार्फत अंमलबजावणी.",
        "portal_url": "https://egs.maharashtra.gov.in",
        "portal_name": "EGS Maharashtra Portal",
        "badge": "💧 सिंचन विहीर अनुदान"
    },
    {
        "id": "scheme-4",
        "title": "सर्वसमावेशक पीक विमा योजना - मात्र ₹१ रुपयात (PM Fasal Bima ₹1 Scheme)",
        "category": "INSURANCE_LOAN",
        "category_title": "विमा व कर्जमाफी",
        "benefit_amount": "मात्र ₹१ रुपयात संपूर्ण पिकाचे विमा संरक्षण",
        "eligibility": "महाराष्ट्रातील सर्व खरीप व रब्बी पीक घेणारे शेतकरी.",
        "description": "शेतकऱ्यांना पीक विम्याचा हप्ता भरावा लागत नाही, फक्त ₹१ भरून विमा नोंदणी करता येते. नैसर्गिक आपत्तीत पीक नुकसानीची भरपाई.",
        "portal_url": "https://pmfby.gov.in",
        "portal_name": "PM Fasal Bima Portal",
        "badge": "🛡️ ₹१ रुपया पीक विमा"
    },
    {
        "id": "scheme-5",
        "title": "भाऊसाहेब फुंडकर फळबाग लागवड योजना (Bhausaheb Fundkar Fruit Scheme)",
        "category": "STATE_SUBSIDY",
        "category_title": "राज्य शासन अनुदान",
        "benefit_amount": "१००% शासकीय अनुदान (३ वर्षांत टप्प्याटप्प्याने)",
        "eligibility": "आंबा, डाळिंब, पेरू, कागदी लिंबू, संत्रा, मोसंबी, काजू लागवड करणारे शेतकरी.",
        "description": "फळबाग लागवडीसाठी खड्डे खोदणे, कलमे खरेदी व ३ वर्षे संगोपणासाठी १००% सबसिडी.",
        "portal_url": "https://krishi.maharashtra.gov.in",
        "portal_name": "MahaAgri Official Portal",
        "badge": "🥭 फळबाग लागवड अनुदान"
    },
    {
        "id": "scheme-6",
        "title": "महाडीबीटी ठिबक व तुषार सिंचन सबसिडी (MahaDBT Drip Irrigation)",
        "category": "SOLAR_IRRIGATION",
        "category_title": "सौर व सिंचन योजना",
        "benefit_amount": "८०% सबसिडी (लहान शेतकरी) व ७५% (इतर शेतकरी)",
        "eligibility": "सूक्ष्म सिंचन (ठिबक/तुषार) संच बसवू इच्छिणारे सर्व शेतकरी.",
        "description": "पाण्याची बचत आणि जास्त पीक उत्पन्नासाठी आधुनिक ठिबक सिंचन संचावर ८० टक्के सबसिडी महाडीबीटी पोर्टलद्वारे जमा.",
        "portal_url": "https://mahadbt.maharashtra.gov.in",
        "portal_name": "MahaDBT Farmer Portal",
        "badge": "💧 महाडीबीटी ठिबक सबसिडी"
    },
    {
        "id": "scheme-7",
        "title": "छत्रपती शिवाजी महाराज शेतकरी सन्मान / ₹५०,००० प्रोत्साहन योजना",
        "category": "INSURANCE_LOAN",
        "category_title": "विमा व कर्जमाफी",
        "benefit_amount": "मुदतीत पीक कर्ज परत करणाऱ्यांना ₹५०,००० पर्यंत प्रोत्साहन अनुदान",
        "eligibility": "नियमितपणे अल्पमुदत पीक कर्जाची परतफेड करणारे प्रामाणिक शेतकरी.",
        "description": "बँकेचे पीककर्ज वेळेवर फेडणाऱ्या शेतकऱ्यांना प्रोत्साहन म्हणून ₹५०,००० थेट बँक खात्यात जमा केले जातात.",
        "portal_url": "https://mjpsky.maharashtra.gov.in",
        "portal_name": "MJPSKY Mahagov Portal",
        "badge": "💰 नियमित कर्ज परतफेड अनुदान"
    },
    {
        "id": "scheme-8",
        "title": "गोपीनाथ मुंडे शेतकरी अपघात सुरक्षा योजना (Accident Insurance Scheme)",
        "category": "INSURANCE_LOAN",
        "category_title": "विमा व कर्जमाफी",
        "benefit_amount": "₹२.०० लाख रुपयांपर्यंत अपघात विमा भरपाई",
        "eligibility": "महाराष्ट्रातील सर्व १० ते ७५ वर्षे वयोगटातील नोंदणीकृत शेतकरी व त्यांचे कुटुंब.",
        "description": "शेतात काम करताना अपघात, विजेचा धक्का, सर्पदंश किंवा वाहनामुळे मृत्यू/अपंगत्व आल्यास कुटुंबीयांना ₹२ लाखांची मदत.",
        "portal_url": "https://krishi.maharashtra.gov.in",
        "portal_name": "Maharashtra Agri Dept",
        "badge": "🏥 शेतकरी अपघात विमा"
    },
    {
        "id": "scheme-9",
        "title": "डॉ. पंजाबराव देशमुख व्याज सवलत योजना (0% Interest Crop Loan)",
        "category": "INSURANCE_LOAN",
        "category_title": "विमा व कर्जमाफी",
        "benefit_amount": "३ लाखांपर्यंतच्या पीक कर्जावर ०% व्याज दर (१००% व्याज सवलत)",
        "eligibility": "राष्ट्रीयीकृत व सहकारी बँकेतून पीककर्ज घेणारे व वेळेत परतफेड करणारे शेतकरी.",
        "description": "३ लाख रुपयांपर्यंतच्या अल्पमुदत पीक कर्जाची वेळेवर परतफेड केल्यास संपूर्ण व्याजाची सवलत शासनाकडून दिली जाते.",
        "portal_url": "https://cooperation.maharashtra.gov.in",
        "portal_name": "Maha Cooperation Dept",
        "badge": "🏦 ०% व्याज पीक कर्ज"
    }
]