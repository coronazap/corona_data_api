#!/usr/bin/python
# -*- coding: utf-8 -*-

from unicodedata import normalize 

countries = [(1, 'AFEGANISTÃO', 'AFGHANISTAN'),
(2, 'ACROTÍRI E DECELIA', 'AKROTIRI E DEKÉLIA'),
(3, 'ÁFRICA DO SUL', 'SOUTH AFRICA'),
(4, 'ALBÂNIA', 'ALBANIA'),
(5, 'ALEMANHA', 'GERMANY'),
(6, 'AMERICAN SAMOA', 'AMERICAN SAMOA'),
(7, 'ANDORRA', 'ANDORRA'),
(8, 'ANGOLA', 'ANGOLA'),
(9, 'ANGUILLA', 'ANGUILLA'),
(10, 'ANTÍGUA E BARBUDA', 'ANTIGUA AND BARBUDA'),
(11, 'ANTILHAS NEERLANDESAS', 'NETHERLANDS ANTILLES'),
(12, 'ARÁBIA SAUDITA', 'SAUDI ARABIA'),
(13, 'ARGÉLIA', 'ALGERIA'),
(14, 'ARGENTINA', 'ARGENTINA'),
(15, 'ARMÉNIA', 'ARMENIA'),
(16, 'ARUBA', 'ARUBA'),
(17, 'AUSTRÁLIA', 'AUSTRALIA'),
(18, 'ÁUSTRIA', 'AUSTRIA'),
(19, 'AZERBAIJÃO', 'AZERBAIJAN'),
(20, 'BAHAMAS', 'BAHAMAS, THE'),
(21, 'BANGLADECHE', 'BANGLADESH'),
(22, 'BARBADOS', 'BARBADOS'),
(23, 'BARÉM', 'BAHRAIN'),
(24, 'BASSAS DA ÍNDIA', 'BASSAS DA INDIA'),
(25, 'BÉLGICA', 'BELGIUM'),
(26, 'BELIZE', 'BELIZE'),
(27, 'BENIM', 'BENIN'),
(28, 'BERMUDAS', 'BERMUDA'),
(29, 'BIELORRÚSSIA', 'BELARUS'),
(30, 'BOLÍVIA', 'BOLIVIA'),
(31, 'BÓSNIA E HERZEGOVINA', 'BOSNIA AND HERZEGOVINA'),
(32, 'BOTSUANA', 'BOTSWANA'),
(33, 'BRASIL', 'BRAZIL'),
(34, 'BRUNEI DARUSSALAM', 'BRUNEI'),
(35, 'BULGÁRIA', 'BULGARIA'),
(36, 'BURQUINA FASO', 'BURKINA FASO'),
(37, 'BURUNDI', 'BURUNDI'),
(38, 'BUTÃO', 'BHUTAN'),
(39, 'CABO VERDE', 'CABO VERDE'),
(40, 'CAMARÕES', 'CAMEROON'),
(41, 'CAMBOJA', 'CAMBODIA'),
(42, 'CANADÁ', 'CANADA'),
(43, 'CATAR', 'QATAR'),
(44, 'CAZAQUISTÃO', 'KAZAKHSTAN'),
(45, 'CENTRO-AFRICANA REPÚBLICA', 'CAR'),
(46, 'CHADE', 'CHAD'),
(47, 'CHILE', 'CHILE'),
(48, 'CHINA', 'CHINA'),
(49, 'CHIPRE', 'CYPRUS'),
(50, 'COLÔMBIA', 'COLOMBIA'),
(51, 'COMORES', 'COMOROS'),
(52, 'CONGO', 'CONGO'),
(53, 'CONGO REPÚBLICA DEMOCRÁTICA', 'DRC'),
(54, 'COREIA DO NORTE', 'N.KOREA'),
(55, 'COREIA DO SUL', 'S.KOREA'),
(56, 'COSTA DO MARFIM', 'IVORY COAST'),
(57, 'COSTA RICA', 'COSTA RICA'),
(58, 'CROÁCIA', 'CROATIA'),
(59, 'CUBA', 'CUBA'),
(60, 'DINAMARCA', 'DENMARK'),
(61, 'DOMÍNICA', 'DOMINICA'),
(62, 'EGITO', 'EGYPT'),
(63, 'EMIRADOS ÁRABES UNIDOS', 'UAE'),
(64, 'EQUADOR', 'ECUADOR'),
(65, 'ERITREIA', 'ERITREA'),
(66, 'ESLOVÁQUIA', 'SLOVAKIA'),
(67, 'ESLOVÉNIA', 'SLOVENIA'),
(68, 'ESPANHA', 'SPAIN'),
(69, 'ESTADOS UNIDOS', 'USA'),
(70, 'ESTÓNIA', 'ESTONIA'),
(71, 'ETIÓPIA', 'ETHIOPIA'),
(72, 'FAIXA DE GAZA', 'GAZA STRIP'),
(73, 'FIJI', 'FIJI'),
(74, 'FILIPINAS', 'PHILIPPINES'),
(75, 'FINLÂNDIA', 'FINLAND'),
(76, 'FRANÇA', 'FRANCE'),
(77, 'GABÃO', 'GABON'),
(78, 'GÂMBIA', 'GAMBIA'),
(79, 'GANA', 'GHANA'),
(80, 'GEÓRGIA', 'GEORGIA'),
(81, 'GIBRALTAR', 'GIBRALTAR'),
(82, 'GRANADA', 'GRENADA'),
(83, 'GRÉCIA', 'GREECE'),
(84, 'GRONELÂNDIA', 'GREENLAND'),
(85, 'GUADALUPE', 'GUADELOUPE'),
(86, 'GUAM', 'GUAM'),
(87, 'GUATEMALA', 'GUATEMALA'),
(88, 'GUERNSEY', 'GUERNSEY'),
(89, 'GUIANA', 'GUYANA'),
(90, 'GUIANA FRANCESA', 'FRENCH GUIANA'),
(91, 'GUINÉ', 'GUINEA'),
(92, 'GUINÉ EQUATORIAL', 'EQUATORIAL GUINEA'),
(93, 'GUINÉ-BISSAU', 'GUINEA-BISSAU'),
(94, 'HAITI', 'HAITI'),
(95, 'HONDURAS', 'HONDURAS'),
(96, 'HONG KONG', 'HONG KONG'),
(96, 'HOLANDA', 'NETHERLANDS'),
(97, 'HUNGRIA', 'HUNGARY'),
(98, 'IÉMEN', 'YEMEN'),
(99, 'ILHA BOUVET', 'BOUVET ISLAND'),
(100, 'ILHA CHRISTMAS', 'CHRISTMAS ISLAND'),
(101, 'ILHA DE CLIPPERTON', 'CLIPPERTON ISLAND'),
(102, 'ILHA DE JOÃO DA NOVA', 'JUAN DE NOVA ISLAND'),
(103, 'ILHA DE MAN', 'ISLE OF MAN'),
(104, 'ILHA DE NAVASSA', 'NAVASSA ISLAND'),
(105, 'ILHA EUROPA', 'EUROPA ISLAND'),
(106, 'ILHA NORFOLK', 'NORFOLK ISLAND'),
(107, 'ILHA TROMELIN', 'TROMELIN ISLAND'),
(108, 'ILHAS ASHMORE E CARTIER', 'ASHMORE AND CARTIER ISLANDS'),
(109, 'ILHAS CAIMAN', 'CAYMAN ISLANDS'),
(110, 'ILHAS COCOS (KEELING)', 'COCOS (KEELING) ISLANDS'),
(111, 'ILHAS COOK', 'COOK ISLANDS'),
(112, 'ILHAS DO MAR DE CORAL', 'CORAL SEA ISLANDS'),
(113, 'ILHAS FALKLANDS (ILHAS MALVINAS)', 'FALKLAND ISLANDS (ISLAS MALVINAS)'),
(114, 'ILHAS FEROE', 'FAEROE ISLANDS'),
(115, 'ILHAS GEÓRGIA DO SUL E SANDWICH DO SUL', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS'),
(116, 'ILHAS MARIANAS DO NORTE', 'NORTHERN MARIANA ISLANDS'),
(117, 'ILHAS MARSHALL', 'MARSHALL ISLANDS'),
(118, 'ILHAS PARACEL', 'PARACEL ISLANDS'),
(119, 'ILHAS PITCAIRN', 'PITCAIRN ISLANDS'),
(120, 'ILHAS SALOMÃO', 'SOLOMON ISLANDS'),
(121, 'ILHAS SPRATLY', 'SPRATLY ISLANDS'),
(122, 'ILHAS VIRGENS AMERICANAS', 'U. S. VIRGIN ISLANDS'),
(123, 'ILHAS VIRGENS BRITÂNICAS', 'BRITISH VIRGIN ISLANDS'),
(124, 'ÍNDIA', 'INDIA'),
(125, 'INDONÉSIA', 'INDONESIA'),
(126, 'IRÃO', 'IRAN'),
(127, 'IRAQUE', 'IRAQ'),
(128, 'IRLANDA', 'IRELAND'),
(129, 'ISLÂNDIA', 'ICELAND'),
(130, 'ISRAEL', 'ISRAEL'),
(131, 'ITÁLIA', 'ITALY'),
(132, 'JAMAICA', 'JAMAICA'),
(133, 'JAN MAYEN', 'JAN MAYEN'),
(134, 'JAPÃO', 'JAPAN'),
(135, 'JERSEY', 'JERSEY'),
(136, 'JIBUTI', 'DJIBOUTI'),
(137, 'JORDÂNIA', 'JORDAN'),
(138, 'KIRIBATI', 'KIRIBATI'),
(139, 'KOWEIT', 'KUWAIT'),
(140, 'LAOS', 'LAOS'),
(141, 'LESOTO', 'LESOTHO'),
(142, 'LETÓNIA', 'LATVIA'),
(143, 'LÍBANO', 'LEBANON'),
(144, 'LIBÉRIA', 'LIBERIA'),
(145, 'LÍBIA', 'LIBYAN ARAB JAMAHIRIYA'),
(146, 'countriesENSTAINE', 'LIECHTENSTEIN'),
(147, 'LITUÂNIA', 'LITHUANIA'),
(148, 'LUXEMBURGO', 'LUXEMBOURG'),
(149, 'MACAU', 'MACAO'),
(150, 'MACEDÓNIA', 'NORTH MACEDONIA'),
(151, 'MADAGÁSCAR', 'MADAGASCAR'),
(152, 'MALÁSIA', 'MALAYSIA'),
(153, 'MALAVI', 'MALAWI'),
(154, 'MALDIVAS', 'MALDIVES'),
(155, 'MALI', 'MALI'),
(156, 'MALTA', 'MALTA'),
(157, 'MARROCOS', 'MOROCCO'),
(158, 'MARTINICA', 'MARTINIQUE'),
(159, 'MAURÍCIA', 'MAURITIUS'),
(160, 'MAURITÂNIA', 'MAURITANIA'),
(161, 'MAYOTTE', 'MAYOTTE'),
(162, 'MÉXICO', 'MEXICO'),
(163, 'MIANMAR', 'MYANMAR BURMA'),
(164, 'MICRONÉSIA', 'MICRONESIA'),
(165, 'MOÇAMBIQUE', 'MOZAMBIQUE'),
(166, 'MOLDÁVIA', 'MOLDOVA'),
(167, 'MÓNACO', 'MONACO'),
(168, 'MONGÓLIA', 'MONGOLIA'),
(169, 'MONTENEGRO', 'MONTENEGRO'),
(170, 'MONTSERRAT', 'MONTSERRAT'),
(171, 'NAMÍBIA', 'NAMIBIA'),
(172, 'NAURU', 'NAURU'),
(173, 'NEPAL', 'NEPAL'),
(174, 'NICARÁGUA', 'NICARAGUA'),
(175, 'NÍGER', 'NIGER'),
(176, 'NIGÉRIA', 'NIGERIA'),
(177, 'NIUE', 'NIUE'),
(178, 'NORUEGA', 'NORWAY'),
(179, 'NOVA CALEDÓNIA', 'NEW CALEDONIA'),
(180, 'NOVA ZELÂNDIA', 'NEW ZEALAND'),
(181, 'OMÃ', 'OMAN'),
(182, 'PAÍSES BAIXOS', 'NETHERLANDS'),
(183, 'PALAU', 'PALAU'),
(184, 'PALESTINA', 'PALESTINE'),
(185, 'PANAMÁ', 'PANAMA'),
(186, 'PAPUÁSIA-NOVA GUINÉ', 'PAPUA NEW GUINEA'),
(187, 'PAQUISTÃO', 'PAKISTAN'),
(188, 'PARAGUAI', 'PARAGUAY'),
(189, 'PERU', 'PERU'),
(190, 'POLINÉSIA FRANCESA', 'FRENCH POLYNESIA'),
(191, 'POLÓNIA', 'POLAND'),
(192, 'PORTO RICO', 'PUERTO RICO'),
(193, 'PORTUGAL', 'PORTUGAL'),
(194, 'QUÉNIA', 'KENYA'),
(195, 'QUIRGUIZISTÃO', 'KYRGYZSTAN'),
(196, 'REINO UNIDO', 'UK'),
(197, 'REPÚBLICA CHECA', 'CZECHIA'),
(198, 'REPÚBLICA DOMINICANA', 'DOMINICAN REPUBLIC'),
(199, 'ROMÉNIA', 'ROMANIA'),
(200, 'RUANDA', 'RWANDA'),
(201, 'RÚSSIA', 'RUSSIA'),
(202, 'SAHARA OCCIDENTAL', 'WESTERN SAHARA'),
(203, 'SALVADOR', 'EL SALVADOR'),
(204, 'SAMOA', 'SAMOA'),
(205, 'SANTA HELENA', 'SAINT HELENA'),
(206, 'SANTA LÚCIA', 'SAINT LUCIA'),
(207, 'SANTA SÉ', 'HOLY SEE'),
(208, 'SÃO CRISTÓVÃO E NEVES', 'SAINT KITTS AND NEVIS'),
(209, 'SÃO MARINO', 'SAN MARINO'),
(210, 'SÃO PEDRO E MIQUELÃO', 'SAINT PIERRE AND MIQUELON'),
(211, 'SÃO TOMÉ E PRÍNCIPE', 'SAO TOME AND PRINCIPE'),
(212, 'SÃO VICENTE E GRANADINAS', 'ST. VINCENT GRENADINES'),
(213, 'SEICHELES', 'SEYCHELLES'),
(214, 'SENEGAL', 'SENEGAL'),
(215, 'SERRA LEOA', 'SIERRA LEONE'),
(216, 'SÉRVIA', 'SERBIA'),
(217, 'SINGAPURA', 'SINGAPORE'),
(218, 'SÍRIA', 'SYRIA'),
(219, 'SOMÁLIA', 'SOMALIA'),
(220, 'SRI LANCA', 'SRI LANKA'),
(221, 'SUAZILÂNDIA', 'SWAZILAND'),
(222, 'SUDÃO', 'SUDAN'),
(223, 'SUÉCIA', 'SWEDEN'),
(224, 'SUÍÇA', 'SWITZERLAND'),
(225, 'SURINAME', 'SURINAME'),
(226, 'SVALBARD', 'SVALBARD'),
(227, 'TAILÂNDIA', 'THAILAND'),
(228, 'TAIWAN', 'TAIWAN'),
(229, 'TAJIQUISTÃO', 'TAJIKISTAN'),
(230, 'TANZÂNIA', 'TANZANIA'),
(231, 'TERRITÓRIO BRITÂNICO DO OCEANO ÍNDICO', 'BRITISH INDIAN OCEAN TERRITORY'),
(232, 'TERRITÓRIO DAS ILHAS HEARD E MCDONALD', 'HEARD ISLAND AND MCDONALD ISLANDS'),
(233, 'TIMOR-LESTE', 'TIMOR-LESTE'),
(234, 'TOGO', 'TOGO'),
(235, 'TOKELAU', 'TOKELAU'),
(236, 'TONGA', 'TONGA'),
(237, 'TRINDADE E TOBAGO', 'TRINIDAD AND TOBAGO'),
(238, 'TUNÍSIA', 'TUNISIA'),
(239, 'TURKS E CAICOS', 'TURKS AND CAICOS ISLANDS'),
(240, 'TURQUEMENISTÃO', 'TURKMENISTAN'),
(241, 'TURQUIA', 'TURKEY'),
(242, 'TUVALU', 'TUVALU'),
(243, 'UCRÂNIA', 'UKRAINE'),
(244, 'UGANDA', 'UGANDA'),
(245, 'URUGUAI', 'URUGUAY'),
(246, 'USBEQUISTÃO', 'UZBEKISTAN'),
(247, 'VANUATU', 'VANUATU'),
(248, 'VENEZUELA', 'VENEZUELA'),
(249, 'VIETNAME', 'VIETNAM'),
(250, 'WALLIS E FUTUNA', 'WALLIS AND FUTUNA'),
(251, 'ZÂMBIA', 'ZAMBIA'),
(252, 'ZIMBABUÉ', 'ZIMBABWE'),
(253, 'DIAMONDPRINCESS', 'DIAMONDPRINCESS'),
(254, 'ILHA DA REUNIÃO', 'REÚNION'), 
(255, 'ILHAS DO CANAL', 'CHANNEL ISLANDS'), 
(256, 'SÃO MARTINHO', 'SAINT MARTIN'), 
(257, 'CURAÇAU', 'CURAÇAO'), 
(258, 'BAHAMAS', 'BAHAMAS'), 
(259, 'SÃO BARTOLOMEU', 'ST.BARTH'), 
(260, 'VATICANO', 'VATICAN CITY'), 
(261, 'ILHAS DE SÃO MARTINHO', 'SINT MAARTEN'), 
(262, 'Essuatíni', 'Eswatini'),
(263, 'MUNDO', 'Total: ',
(264, 'MYANMAR','BIRMÂNIA')) ]

en_to_pt = {}

for item in countries: 
    pt_name = normalize('NFKD', item[1].lower()).encode('ASCII', 'ignore').decode('ASCII')
    en_name = normalize('NFKD', item[2].lower().replace(' ','')).encode('ASCII', 'ignore').decode('ASCII')
    en_to_pt[en_name] = pt_name


def get_pt_name(en_name): 

    try:
        formatted_en_name = normalize('NFKD', en_name).encode('ASCII', 'ignore').decode('ASCII').lower()       
        return en_to_pt[formatted_en_name]
    except: 
        return 'others'
        
    