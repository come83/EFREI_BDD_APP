DROP TABLE IF EXISTS ecole_cfa_apprenti;
DROP TABLE IF EXISTS apprenti;
DROP TABLE IF EXISTS diplome;
DROP TABLE IF EXISTS specialite;
DROP TABLE IF EXISTS entreprise;
DROP TABLE IF EXISTS ecole;
DROP TABLE IF EXISTS cfa;
DROP TABLE IF EXISTS organisme;

CREATE TABLE Organisme (
    id_organisme INTEGER PRIMARY KEY AUTO_INCREMENT,

    id_og INTEGER NOT NULL,
    libelle_organisme VARCHAR(255)
);

CREATE TABLE CFA (
    id_cfa INTEGER PRIMARY KEY AUTO_INCREMENT,

    id_etab INTEGER,
    nom_complet_cfa VARCHAR(255),

    id_organisme INTEGER,
    CONSTRAINT FOREIGN KEY (id_organisme) REFERENCES Organisme (id_organisme)
);

CREATE TABLE Ecole ( 
    id_ecole INTEGER PRIMARY KEY AUTO_INCREMENT,

    duree_formation_mois INTEGER,
    annee_formation INTEGER,
    id_siteformation INTEGER,
    libelle_lien_cfa VARCHAR(255),
    nom_site_formation VARCHAR(255),         
    adresse1_site VARCHAR(255),   
    code_postal_site INTEGER,
    libelle_ville_site VARCHAR(255)

    -- id_cfa INTEGER,
    -- CONSTRAINT FOREIGN KEY (id_cfa) REFERENCES CFA (id_cfa)
);

CREATE TABLE Entreprise (
    id_entreprise INTEGER PRIMARY KEY AUTO_INCREMENT,

    code_naf_entreprise INTEGER,
    depart_entreprise INTEGER, -- departement
    code_insee_entreprise INTEGER          
);

CREATE TABLE Specialite (
    id_specialite INTEGER PRIMARY KEY AUTO_INCREMENT,

    code_groupe_specialite INTEGER,
    libelle_specialite_com VARCHAR(255) NOT NULL,
    libelle_specialite VARCHAR(255) NOT NULL
);

CREATE TABLE Diplome (
    id_diplome INTEGER PRIMARY KEY AUTO_INCREMENT,

    diplome INTEGER, -- diplome
    libelle_diplome VARCHAR(255) NOT NULL,
    type_diplome VARCHAR(255) NOT NULL,     

    id_ecole INTEGER,
    id_specialite INTEGER,
    CONSTRAINT FOREIGN KEY (id_ecole) REFERENCES Ecole (id_ecole),
    CONSTRAINT FOREIGN KEY (id_specialite) REFERENCES Specialite (id_specialite)

);

CREATE TABLE Apprenti (
    id_apprenti INTEGER PRIMARY KEY AUTO_INCREMENT,

    sexe VARCHAR(255),
    age_jeune_decembre INTEGER,
    handicap_oui_non_vide VARCHAR(255),
    libelle_qualite VARCHAR(255),
    libelle_ville_jeune VARCHAR(255),
    libelle_pcs_parent VARCHAR(255),
    code_postal_jeune INTEGER,
    libelle_nationalite VARCHAR(255),
    libelle_origine_prec_cfa VARCHAR(255),
    libelle_origine_annee_prec VARCHAR(255),

    -- id_ecole INTEGER,
    id_entreprise INTEGER,
    id_diplome INTEGER,
    -- CONSTRAINT FOREIGN KEY (id_ecole) REFERENCES Ecole (id_ecole),
    CONSTRAINT FOREIGN KEY (id_entreprise) REFERENCES Entreprise (id_entreprise),
    CONSTRAINT FOREIGN KEY (id_diplome) REFERENCES Diplome (id_diplome)         


);

CREATE TABLE Ecole_CFA_Apprenti(
    id_ecole INTEGER,
    id_cfa INTEGER,
    id_apprenti INTEGER,

    PRIMARY KEY (id_ecole, id_cfa, id_apprenti),
    FOREIGN KEY (id_ecole) REFERENCES Ecole(id_ecole),
    FOREIGN KEY (id_cfa) REFERENCES CFA(id_cfa),
    FOREIGN KEY (id_apprenti) REFERENCES Apprenti(id_apprenti)
) ;

