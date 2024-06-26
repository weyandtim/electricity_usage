.. _click-ref:

Click CLI
=====================================

The :program:`electricity_usage` command accepts the following subcommands: ``start``, ``stop``, ``run``, ``areas``, ``queue``. If none of these are used, the program defaults to the ``--help`` option.

.. click:: electricity_usage.__main__:cli
    :prog: electricity_usage
    :nested: short

Subcommands
--------------------------------------

.. click:: electricity_usage.commands.start:start
    :prog: start
    :nested: short

The options for :option:`--area` correspond to the area codes used by the Electricity Maps API.

:option:`--em_auth_token` accepts your Electricity Maps auth token as a ``string`` 

.. click:: electricity_usage.commands.run:run
    :prog: run
    :nested: full

:option:`--estimate` accepts a ``string`` formatted as accepted by `pytimeparse`_.

.. _pytimeparse: https://pypi.org/project/pytimeparse/

:option:`--deadline` accepts dates and timestamps in the following formats: '%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S' 

:option:`--commandline` accepts a ``string``, which will be executed as a shell command

.. click:: electricity_usage.commands.stop:stop
    :prog: stop
    :nested: full

.. click:: electricity_usage.commands.status:status
    :prog: status
    :nested: full

.. click:: electricity_usage.commands.areas:areas
    :prog: areas
    :nested: full

Areas as provided by Electricity Maps
-----------------------------------------------------------------------

.. list-table:: Area Codes and corresponding area as provided by Electricity Maps
   :widths: 25 75
   :header-rows: 1
   
   * - Code
     - Corresponding area
   * - AD
     - Andorra
   * - AE
     - United Arab Emirates
   * - AF
     - Afghanistan
   * - AG
     - Antigua and Barbuda
   * - AL
     - Albania
   * - AM
     - Armenia
   * - AO
     - Angola
   * - AR
     - Argentina
   * - AT
     - Austria
   * - AU
     - Australia
   * - AU-LH
     - Lord Howe Island
   * - AU-NSW
     - New South Wales
   * - AU-NT
     - Northern Territory
   * - AU-QLD
     - Queensland
   * - AU-SA
     - South Australia
   * - AU-TAS
     - Tasmania
   * - AU-TAS-CBI
     - Cape Barren Island
   * - AU-TAS-FI
     - Flinders Island
   * - AU-TAS-KI
     - King Island
   * - AU-VIC
     - Victoria
   * - AU-WA
     - Western Australia
   * - AU-WA-RI
     - Rottnest Island
   * - AW
     - Aruba
   * - AX
     - Åland Islands
   * - AZ
     - Azerbaijan
   * - BA
     - Bosnia and Herzegovina
   * - BB
     - Barbados
   * - BD
     - Bangladesh
   * - BE
     - Belgium
   * - BF
     - Burkina Faso
   * - BG
     - Bulgaria
   * - BH
     - Bahrain
   * - BI
     - Burundi
   * - BJ
     - Benin
   * - BN
     - Brunei
   * - BO
     - Bolivia
   * - BR
     - Brazil
   * - BR-CS
     - Central Brazil
   * - BR-N
     - North Brazil
   * - BR-NE
     - North-East Brazil
   * - BR-S
     - South Brazil
   * - BS
     - Bahamas
   * - BT
     - Bhutan
   * - BW
     - Botswana
   * - BY
     - Belarus
   * - BZ
     - Belize
   * - CA-AB
     - Alberta
   * - CA-BC
     - British Columbia
   * - CA-MB
     - Manitoba
   * - CA-NB
     - New Brunswick
   * - CA-NL-LB
     - Labrador
   * - CA-NL-NF
     - Newfoundland
   * - CA-NS
     - Nova Scotia
   * - CA-NT
     - Northwest Territories
   * - CA-NU
     - Nunavut
   * - CA-ON
     - Ontario
   * - CA-PE
     - Prince Edward Island
   * - CA-QC
     - Québec
   * - CA-SK
     - Saskatchewan
   * - CA-YT
     - Yukon
   * - CD
     - Democratic Republic of the Congo
   * - CF
     - Central African Republic
   * - CG
     - Congo
   * - CH
     - Switzerland
   * - CI
     - Ivory Coast
   * - CL-CHP
     - Easter Island
   * - CL-SEA
     - Sistema Eléctrico de Aysén
   * - CL-SEM
     - Sistema Eléctrico de Magallanes
   * - CL-SEN
     - Sistema Eléctrico Nacional
   * - CM
     - Cameroon
   * - CN
     - China
   * - CO
     - Colombia
   * - CR
     - Costa Rica
   * - CU
     - Cuba
   * - CV
     - Cabo Verde
   * - CY
     - Cyprus
   * - CZ
     - Czechia
   * - DE
     - Germany
   * - DJ
     - Djibouti
   * - DK
     - Denmark
   * - DK-BHM
     - Bornholm
   * - DK-DK1
     - West Denmark
   * - DK-DK2
     - East Denmark
   * - DM
     - Dominica
   * - DO
     - Dominican Republic
   * - DZ
     - Algeria
   * - EC
     - Ecuador
   * - EE
     - Estonia
   * - EG
     - Egypt
   * - EH
     - Western Sahara
   * - ER
     - Eritrea
   * - ES
     - Spain
   * - ES-CE
     - Ceuta
   * - ES-CN-FVLZ
     - Fuerteventura/Lanzarote
   * - ES-CN-GC
     - Gran Canaria
   * - ES-CN-HI
     - El Hierro
   * - ES-CN-IG
     - Isla de la Gomera
   * - ES-CN-LP
     - La Palma
   * - ES-CN-TE
     - Tenerife
   * - ES-IB-FO
     - Formentera
   * - ES-IB-IZ
     - Ibiza
   * - ES-IB-MA
     - Mallorca
   * - ES-IB-ME
     - Menorca
   * - ES-ML
     - Melilla
   * - ET
     - Ethiopia
   * - FI
     - Finland
   * - FJ
     - Fiji
   * - FK
     - Falkland Islands
   * - FM
     - Micronesia
   * - FO
     - Faroe Islands
   * - FO-MI
     - Main Islands
   * - FO-SI
     - South Island
   * - FR
     - France
   * - FR-COR
     - Corsica
   * - GA
     - Gabon
   * - GB
     - Great Britain
   * - GB-NIR
     - Northern Ireland
   * - GB-ORK
     - Orkney Islands
   * - GB-ZET
     - Unknown
   * - GE
     - Georgia
   * - GF
     - French Guiana
   * - GH
     - Ghana
   * - GL
     - Greenland
   * - GM
     - Gambia
   * - GN
     - Guinea
   * - GP
     - Guadeloupe
   * - GQ
     - Equatorial Guinea
   * - GR
     - Greece
   * - GR-IS
     - Aegean Islands
   * - GS
     - South Georgia and the South Sandwich Islands
   * - GT
     - Guatemala
   * - GU
     - Guam
   * - GW
     - Guinea-Bissau
   * - GY
     - Guyana
   * - HK
     - Hong Kong
   * - HM
     - Heard Island and McDonald Islands
   * - HN
     - Honduras
   * - HR
     - Croatia
   * - HT
     - Haiti
   * - HU
     - Hungary
   * - ID
     - Indonesia
   * - IE
     - Ireland
   * - IL
     - Israel
   * - IM
     - Isle of Man
   * - IN
     - Mainland India
   * - IN-AN
     - Andaman and Nicobar Islands
   * - IN-DL
     - Delhi
   * - IN-EA
     - Eastern India
   * - IN-HP
     - Himachal Pradesh
   * - IN-KA
     - Karnataka
   * - IN-MH
     - Maharashtra
   * - IN-NE
     - North Eastern India
   * - IN-NO
     - Northern India
   * - IN-PB
     - Punjab
   * - IN-SO
     - Southern India
   * - IN-UP
     - Uttar Pradesh
   * - IN-UT
     - Uttarakhand
   * - IN-WE
     - Western India
   * - IQ
     - Iraq
   * - IQ-KUR
     - Kurdistan
   * - IR
     - Iran
   * - IS
     - Iceland
   * - IT
     - Italy
   * - IT-CNO
     - Central North Italy
   * - IT-CSO
     - Central South Italy
   * - IT-NO
     - North Italy
   * - IT-SAR
     - Sardinia
   * - IT-SIC
     - Sicily
   * - IT-SO
     - South Italy
   * - JM
     - Jamaica
   * - JO
     - Jordan
   * - JP
     - Japan
   * - JP-CB
     - Chūbu
   * - JP-CG
     - Chūgoku
   * - JP-HKD
     - Hokkaidō
   * - JP-HR
     - Hokuriku
   * - JP-KN
     - Kansai
   * - JP-KY
     - Kyūshū
   * - JP-ON
     - Okinawa
   * - JP-SK
     - Shikoku
   * - JP-TH
     - Tōhoku
   * - JP-TK
     - Tōkyō
   * - KE
     - Kenya
   * - KG
     - Kyrgyzstan
   * - KH
     - Cambodia
   * - KM
     - Comoros
   * - KP
     - North Korea
   * - KR
     - South Korea
   * - KW
     - Kuwait
   * - KZ
     - Kazakhstan
   * - LA
     - Laos
   * - LB
     - Lebanon
   * - LC
     - Saint Lucia
   * - LI
     - Liechtenstein
   * - LK
     - Sri Lanka
   * - LR
     - Liberia
   * - LS
     - Lesotho
   * - LT
     - Lithuania
   * - LU
     - Luxembourg
   * - LV
     - Latvia
   * - LY
     - Libya
   * - MA
     - Morocco
   * - MD
     - Moldova
   * - ME
     - Montenegro
   * - MG
     - Madagascar
   * - MK
     - North Macedonia
   * - ML
     - Mali
   * - MM
     - Myanmar
   * - MN
     - Mongolia
   * - MQ
     - Martinique
   * - MR
     - Mauritania
   * - MT
     - Malta
   * - MU
     - Mauritius
   * - MW
     - Malawi
   * - MX
     - Mexico
   * - MX-BC
     - Baja California
   * - MX-BCS
     - Baja California Sur
   * - MX-CE
     - Central
   * - MX-NE
     - North East
   * - MX-NO
     - North
   * - MX-NW
     - North West
   * - MX-OC
     - Occidental
   * - MX-OR
     - Oriental
   * - MX-PN
     - Peninsula
   * - MY-EM
     - Borneo
   * - MY-WM
     - Peninsula
   * - MZ
     - Mozambique
   * - NA
     - Namibia
   * - NC
     - New Caledonia
   * - NE
     - Niger
   * - NG
     - Nigeria
   * - NI
     - Nicaragua
   * - NKR
     - Nagorno-Karabakh
   * - NL
     - Netherlands
   * - NO
     - Norway
   * - NO-NO1
     - Southeast Norway
   * - NO-NO2
     - Southwest Norway
   * - NO-NO3
     - Middle Norway
   * - NO-NO4
     - North Norway
   * - NO-NO5
     - West Norway
   * - NP
     - Nepal
   * - NZ
     - New Zealand
   * - NZ-NZA
     - Auckland Islands
   * - NZ-NZC
     - Chatham Islands
   * - NZ-NZST
     - Stewart Island
   * - OM
     - Oman
   * - PA
     - Panama
   * - PE
     - Peru
   * - PF
     - French Polynesia
   * - PG
     - Papua New Guinea
   * - PH
     - Philippines
   * - PH-LU
     - Luzon
   * - PH-MI
     - Mindanao
   * - PH-VI
     - Visayas
   * - PK
     - Pakistan
   * - PL
     - Poland
   * - PM
     - Saint Pierre and Miquelon
   * - PR
     - Puerto Rico
   * - PS
     - State of Palestine
   * - PT
     - Portugal
   * - PT-AC
     - Azores
   * - PT-MA
     - Madeira
   * - PW
     - Palau
   * - PY
     - Paraguay
   * - QA
     - Qatar
   * - RE
     - Réunion
   * - RO
     - Romania
   * - RS
     - Serbia
   * - RU
     - Russia
   * - RU-1
     - Europe-Ural
   * - RU-2
     - Siberia
   * - RU-AS
     - East
   * - RU-EU
     - Arctic
   * - RU-FE
     - Far East
   * - RU-KGD
     - Kaliningrad
   * - RW
     - Rwanda
   * - SA
     - Saudi Arabia
   * - SB
     - Solomon Islands
   * - SD
     - Sudan
   * - SE
     - Sweden
   * - SE-SE1
     - North Sweden
   * - SE-SE2
     - North Central Sweden
   * - SE-SE3
     - South Central Sweden
   * - SE-SE4
     - South Sweden
   * - SG
     - Singapore
   * - SI
     - Slovenia
   * - SJ
     - Svalbard and Jan Mayen
   * - SK
     - Slovakia
   * - SL
     - Sierra Leone
   * - SN
     - Senegal
   * - SO
     - Somalia
   * - SR
     - Suriname
   * - SS
     - South Sudan
   * - ST
     - Sao Tome and Principe
   * - SV
     - El Salvador
   * - SY
     - Syria
   * - SZ
     - Swaziland
   * - TD
     - Chad
   * - TF
     - French Southern Territories
   * - TG
     - Togo
   * - TH
     - Thailand
   * - TJ
     - Tajikistan
   * - TL
     - Timor-Leste
   * - TM
     - Turkmenistan
   * - TN
     - Tunisia
   * - TO
     - Tonga
   * - TR
     - Turkey
   * - TT
     - Trinidad and Tobago
   * - TW
     - Taiwan
   * - TZ
     - Tanzania
   * - UA
     - Ukraine
   * - UA-CR
     - Crimea
   * - UG
     - Uganda
   * - US
     - Contiguous United States
   * - US-AK
     - Alaska
   * - US-CAL-BANC
     - Balancing Authority Of Northern California
   * - US-CAL-CISO
     - California Independent System Operator
   * - US-CAL-IID
     - Imperial Irrigation District
   * - US-CAL-LDWP
     - Los Angeles Department Of Water And Power
   * - US-CAL-TIDC
     - Turlock Irrigation District
   * - US-CAR-CPLE
     - Duke Energy Progress East
   * - US-CAR-CPLW
     - Duke Energy Progress West
   * - US-CAR-DUK
     - Duke Energy Carolinas
   * - US-CAR-SC
     - South Carolina Public Service Authority
   * - US-CAR-SCEG
     - South Carolina Electric & Gas Company
   * - US-CAR-YAD
     - Alcoa Power Generating, Inc. Yadkin Division
   * - US-CENT-SPA
     - Southwestern Power Administration
   * - US-CENT-SWPP
     - Southwest Power Pool
   * - US-FLA-FMPP
     - Florida Municipal Power Pool
   * - US-FLA-FPC
     - Duke Energy Florida Inc
   * - US-FLA-FPL
     - Florida Power & Light Company
   * - US-FLA-GVL
     - Gainesville Regional Utilities
   * - US-FLA-HST
     - City Of Homestead
   * - US-FLA-JEA
     - Jacksonville Electric Authority
   * - US-FLA-SEC
     - Seminole Electric Cooperative
   * - US-FLA-TAL
     - City Of Tallahassee
   * - US-FLA-TEC
     - Tampa Electric Company
   * - US-HI-HA
     - Hawaii
   * - US-HI-KA
     - Kauai
   * - US-HI-KH
     - Kahoolawe
   * - US-HI-LA
     - Lanai
   * - US-HI-MA
     - Maui
   * - US-HI-MO
     - Molokai
   * - US-HI-NI
     - Niihau
   * - US-HI-OA
     - Oahu
   * - US-MIDA-PJM
     - PJM Interconnection, Llc
   * - US-MIDW-AECI
     - Associated Electric Cooperative, Inc.
   * - US-MIDW-LGEE
     - Louisville Gas And Electric Company And Kentucky Utilities
   * - US-MIDW-MISO
     - Midcontinent Independent Transmission System Operator, Inc.
   * - US-NE-ISNE
     - Iso New England Inc.
   * - US-NW-AVA
     - Avista Corporation
   * - US-NW-BPAT
     - Bonneville Power Administration
   * - US-NW-CHPD
     - PUD No. 1 Of Chelan County
   * - US-NW-DOPD
     - PUD No. 1 Of Douglas County
   * - US-NW-GCPD
     - PUD No. 2 Of Grant County, Washington
   * - US-NW-GRID
     - Gridforce Energy Management, Llc
   * - US-NW-IPCO
     - Idaho Power Company
   * - US-NW-NEVP
     - Nevada Power Company
   * - US-NW-NWMT
     - Northwestern Energy
   * - US-NW-PACE
     - Pacificorp East
   * - US-NW-PACW
     - Pacificorp West
   * - US-NW-PGE
     - Portland General Electric Company
   * - US-NW-PSCO
     - Public Service Company Of Colorado
   * - US-NW-PSEI
     - Puget Sound Energy
   * - US-NW-SCL
     - Seattle City Light
   * - US-NW-TPWR
     - City Of Tacoma, Department Of Public Utilities, Light Division
   * - US-NW-WACM
     - Western Area Power Administration - Rocky Mountain Region
   * - US-NW-WAUW
     - Western Area Power Administration UGP West
   * - US-NY-NYIS
     - New York Independent System Operator
   * - US-SE-SEPA
     - Southeastern Power Administration
   * - US-SE-SOCO
     - Southern Company Services, Inc. - Trans
   * - US-SW-AZPS
     - Arizona Public Service Company
   * - US-SW-EPE
     - El Paso Electric Company
   * - US-SW-PNM
     - Public Service Company Of New Mexico
   * - US-SW-SRP
     - Salt River Project
   * - US-SW-TEPC
     - Tucson Electric Power Company
   * - US-SW-WALC
     - Western Area Power Administration - Desert Southwest Region
   * - US-TEN-TVA
     - Tennessee Valley Authority
   * - US-TEX-ERCO
     - Electric Reliability Council Of Texas, Inc.
   * - UY
     - Uruguay
   * - UZ
     - Uzbekistan
   * - VC
     - Saint Vincent and the Grenadines
   * - VE
     - Venezuela
   * - VI
     - Virgin Islands
   * - VN
     - Vietnam
   * - VN-C
     - Central Vietnam
   * - VN-N
     - Northern Vietnam
   * - VN-S
     - Southern Vietnam
   * - VU
     - Vanuatu
   * - WS
     - Samoa
   * - XK
     - Kosovo
   * - XX
     - Northern Cyprus
   * - YE
     - Yemen
   * - YT
     - Mayotte
   * - ZA
     - South Africa
   * - ZM
     - Zambia
   * - ZW
     - Zimbabwe

