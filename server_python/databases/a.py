# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
# pylint: disable=E0401
# pylint: disable=C0413
# pylint: disable=C0411
# pylint: disable=W0611
# pylint: disable=W1309


data = {
    "alleninstitute_comprehend_medical": {
        "columns": [
            "paper_id",
            "date",
            "dx_name",
            "test_name",
            "procedure_name",
            "phone_or_fax",
            "time_to_test_name",
            "url",
            "generic_name",
            "name",
            "brand_name",
            "address",
            "id",
            "treatment_name",
            "system_organ_site",
            "time_to_treatment_name",
            "time_to_dx_name",
            "time_to_medication_name",
            "time_to_procedure_name",
            "profession",
            "email",
            "age"
        ],
        "description": "The table \"alleninstitute_comprehend_medical\" contains information related to medical data extracted from various sources such as research papers, clinical notes, and other medical documents. \n\n- 'paper_id': Unique identifier for the source document or research paper.\n- 'date': Date associated with the medical information.\n- 'dx_name': Diagnosis name or medical condition.\n- 'test_name': Name of the medical test conducted.\n- 'procedure_name': Name of the medical procedure performed.\n- 'phone_or_fax': Contact information such as phone number or fax.\n- 'time_to_test_name': Time taken to conduct the test.\n- 'url': URL link related to the medical information.\n- 'generic_name': Generic name of a medication.\n- 'name': Name of the individual associated with the medical information.\n- 'brand_name': Brand name of a medication.\n- 'address': Address information related to the medical data.\n- 'id': Identification number or code.\n- 'treatment_name': Name of the medical treatment administered.\n- 'system_organ_site': Specific organ or system within the body related to the medical information.\n- 'time_to_treatment_name': Time taken for the treatment to show effect.\n- 'time_to_dx_name': Time to diagnosis.\n- 'time_to_medication_name': Time to medication.\n- 'time_to_procedure_name': Time to procedure.\n- 'profession': Profession of the individual associated with the medical information.\n- 'email': Email address of the individual associated with the medical information.\n- 'age': Age of the individual associated with the medical information.",
        "joins": [{'table': 'alleninstitute_metadata', 'column': 'url'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "alleninstitute_metadata": {
        "columns": [
            "cord_uid",
            "sha",
            "source_x",
            "title",
            "doi",
            "pmcid",
            "pubmed_id",
            "license",
            "abstract",
            "publish_time",
            "authors",
            "journal",
            "microsoft academic paper id",
            "who #covidence",
            "has_full_text",
            "full_text_file",
            "url"
        ],
        "description": "The table \"alleninstitute_metadata\" contains metadata information related to research articles. Each row in the table represents a single research article and includes the following columns:\n\n1. cord_uid: Unique identifier for the article within the database.\n2. sha: SHA identifier for the article.\n3. source_x: Source of the article.\n4. title: Title of the research article.\n5. doi: Digital Object Identifier for the article.\n6. pmcid: PubMed Central ID for the article.\n7. pubmed_id: PubMed ID for the article.\n8. license: License information for the article.\n9. abstract: Abstract of the research article.\n10. publish_time: Publication time of the article.\n11. authors: Authors of the research article.\n12. journal: Journal where the article was published.\n13. microsoft academic paper id: Microsoft Academic ID for the article.\n14. who #covidence: COVidence ID assigned by the World Health Organization.\n15. has_full_text: Indicates whether the full text of the article is available.\n16. full_text_file: File containing the full text of the article.\n17. url: URL link to access the article online.\n\nOverall, the \"alleninstitute_metadata\" table provides",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'url'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'title'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'doi'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'pmcid'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'publish_time'}]
    },
    "aspirevc_crowd_tracing": {
        "columns": [
            "scandate",
            "scannerdeviceid",
            "scannerdevice_zipcode",
            "location_maxcapacity",
            "location_capacity_enforcedlimit",
            "location_op_hours",
            "userdeviceid",
            "type_of_scan",
            "userid",
            "duration",
            "risklevel",
            "accesslevel",
            "readingtype",
            "temp",
            "o2",
            "symptoms",
            "diagnosed",
            "contact",
            "near",
            "m_score",
            "s_score",
            "result"
        ],
        "description": "The table \"aspirevc_crowd_tracing\" contains data related to crowd tracing activities for a specific location. Here is a description of each column:\n\n1. scandate: The date and time when the scanning took place.\n2. scannerdeviceid: The unique identifier of the scanning device used.\n3. scannerdevice_zipcode: The zipcode of the location where the scanning device is installed.\n4. location_maxcapacity: The maximum capacity of the location.\n5. location_capacity_enforcedlimit: Whether the location enforces a capacity limit.\n6. location_op_hours: The operating hours of the location.\n7. userdeviceid: The unique identifier of the user's device.\n8. type_of_scan: The type of scan conducted (e.g., temperature scan, oxygen level scan).\n9. userid: The unique identifier of the user.\n10. duration: The duration of the scan.\n11. risklevel: The level of risk associated with the scan results.\n12. accesslevel: The access level granted based on the scan results.\n13. readingtype: The type of reading taken during the scan.\n14. temp: The temperature reading of the user.\n15. o2: The oxygen level reading of the user.",
        "joins": []
    },
    "aspirevc_crowd_tracing_zipcode_3digits": {
        "columns": [
            "zip",
            "state"
        ],
        "description": "The table \"aspirevc_crowd_tracing_zipcode_3digits\" contains information about zip codes and their corresponding states. It includes two columns:\n\n1. 'zip': This column stores the 3-digit zip code information. Zip codes are used to identify specific geographic areas within a state.\n\n2. 'state': This column stores the state information corresponding to each zip code. States are the primary administrative divisions within a country.\n\nThis table is likely used for crowd tracing purposes, where the zip code and state information can be utilized to track and analyze the movement or distribution of people within specific geographic regions. It can be valuable for demographic analysis, targeted marketing campaigns, resource allocation, and various other data-driven decision-making processes.",
        "joins": [{'table': 'county_populations', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'state'}, {'table': 'nytimes_counties', 'column': 'state'}, {'table': 'nytimes_states', 'column': 'state'}, {'table': 'us_state_abbreviations', 'column': 'state'}]
    },
    "cdc_moderna_vaccine_distribution": {
        "columns": [
            "jurisdiction",
            "week_of_allocations",
            "first_dose_allocations",
            "second_dose_allocations"
        ],
        "description": "The table \"cdc_moderna_vaccine_distribution\" contains data related to the distribution of Moderna COVID-19 vaccine doses to different jurisdictions. \n\n1. 'jurisdiction': This column stores the name of the jurisdiction to which the vaccine doses are allocated. Jurisdictions could be states, territories, or other administrative regions.\n\n2. 'week_of_allocations': This column indicates the specific week during which the vaccine doses are allocated to the respective jurisdictions. It helps in tracking the distribution timeline.\n\n3. 'first_dose_allocations': This column records the number of first dose allocations of the Moderna vaccine for each jurisdiction in a given week. It represents the initial dose of the vaccine administered to individuals.\n\n4. 'second_dose_allocations': This column contains the number of second dose allocations of the Moderna vaccine for each jurisdiction in a given week. It represents the follow-up dose required for individuals who have already received the first dose.\n\nOverall, this table provides a detailed breakdown of Moderna vaccine distribution by jurisdiction and week, including the allocation of first and second doses. It serves as a valuable resource for monitoring and analyzing the distribution of COVID-19 vaccines across different regions.",
        "joins": [{'table': 'cdc_pfizer_vaccine_distribution', 'column': 'jurisdiction'}, {'table': 'cdc_pfizer_vaccine_distribution', 'column': 'week_of_allocations'}, {'table': 'cdc_pfizer_vaccine_distribution', 'column': 'first_dose_allocations'}, {'table': 'cdc_pfizer_vaccine_distribution', 'column': 'second_dose_allocations'}]
    },
    "cdc_pfizer_vaccine_distribution": {
        "columns": [
            "jurisdiction",
            "week_of_allocations",
            "first_dose_allocations",
            "second_dose_allocations"
        ],
        "description": "The table \"cdc_pfizer_vaccine_distribution\" contains information related to the distribution of the Pfizer-BioNTech COVID-19 vaccine by jurisdiction. \n\n1. jurisdiction: This column stores the name of the jurisdiction where the vaccine allocations are being distributed. Jurisdictions could be states, territories, or other administrative regions.\n\n2. week_of_allocations: This column indicates the specific week during which the vaccine allocations are being distributed. It helps in tracking the timeline of vaccine distribution.\n\n3. first_dose_allocations: This column records the number of first doses of the Pfizer-BioNTech COVID-19 vaccine allocated to each jurisdiction for a particular week. It represents the initial dose of the two-dose vaccination series.\n\n4. second_dose_allocations: This column captures the number of second doses of the Pfizer-BioNTech COVID-19 vaccine allocated to each jurisdiction for a specific week. It signifies the second dose required to complete the vaccination series.\n\nOverall, this table provides a detailed breakdown of Pfizer vaccine allocations by jurisdiction and week, including the number of first and second doses allocated, facilitating monitoring and management of vaccine distribution efforts.",
        "joins": [{'table': 'cdc_moderna_vaccine_distribution', 'column': 'jurisdiction'}, {'table': 'cdc_moderna_vaccine_distribution', 'column': 'week_of_allocations'}, {'table': 'cdc_moderna_vaccine_distribution', 'column': 'first_dose_allocations'}, {'table': 'cdc_moderna_vaccine_distribution', 'column': 'second_dose_allocations'}]
    },
    "country_codes": {
        "columns": [
            "country",
            "alpha-2 code",
            "alpha-3 code",
            "numeric code",
            "latitude",
            "longitude"
        ],
        "description": "The table \"country_codes\" contains information about different countries and their corresponding country codes. \n\n1. 'country': This column stores the names of the countries.\n2. 'alpha-2 code': This column contains the two-letter country codes as defined in ISO 3166-1 alpha-2 standard.\n3. 'alpha-3 code': This column contains the three-letter country codes as defined in ISO 3166-1 alpha-3 standard.\n4. 'numeric code': This column stores the numeric country codes as defined in ISO 3166-1 numeric standard.\n5. 'latitude': This column stores the latitude coordinates of the centroid of the country.\n6. 'longitude': This column stores the longitude coordinates of the centroid of the country.\n\nThe table \"country_codes\" serves as a reference for mapping countries to their respective codes and geographical coordinates. It can be used in various applications such as geographic information systems, data analysis, and international data exchange where accurate country identification and location information are required.",
        "joins": [{'table': 'covid_knowledge_graph_nodes_institution', 'column': 'country'}, {'table': 'enigma_jhu', 'column': 'latitude'}, {'table': 'enigma_jhu', 'column': 'longitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'latitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'longitude'}, {'table': 'hospital_beds', 'column': 'latitude'}, {'table': 'owid_world_vaccinations', 'column': 'country'}, {'table': 'prediction_models_severity_index', 'column': 'latitude'}, {'table': 'prediction_models_severity_index', 'column': 'longitude'}]
    },
    "county_populations": {
        "columns": [
            "id",
            "id2",
            "county",
            "state",
            "population estimate 2018"
        ],
        "description": "The table \"county_populations\" contains information about the population estimates for different counties in various states for the year 2018. \n\n1. 'id': This column serves as a unique identifier for each record in the table.\n2. 'id2': Another identifier column that may be used for additional reference or linking to other datasets.\n3. 'county': This column stores the names of the counties for which the population estimates are provided.\n4. 'state': Indicates the state to which the county belongs.\n5. 'population estimate 2018': This column contains the estimated population count for each county in the year 2018.\n\nThe table \"county_populations\" is structured to facilitate analysis and comparison of population data across different counties and states for the specified year.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'aspirevc_crowd_tracing_zipcode_3digits', 'column': 'state'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_testing_states_daily', 'column': 'state'}, {'table': 'nytimes_counties', 'column': 'county'}, {'table': 'nytimes_counties', 'column': 'state'}, {'table': 'nytimes_states', 'column': 'state'}, {'table': 'us_state_abbreviations', 'column': 'state'}]
    },
    "covid_knowledge_graph_edges": {
        "columns": [
            "id",
            "label",
            "from",
            "to",
            "score"
        ],
        "description": "The table \"covid_knowledge_graph_edges\" contains information about the relationships between entities in a knowledge graph related to COVID-19. \n\n- 'id': This column stores a unique identifier for each edge in the knowledge graph.\n- 'label': This column specifies the type of relationship between two entities connected by the edge.\n- 'from': This column indicates the entity from which the edge originates.\n- 'to': This column indicates the entity to which the edge points.\n- 'score': This column represents a numerical value that indicates the strength or relevance of the relationship between the two entities connected by the edge.\n\nOverall, the table \"covid_knowledge_graph_edges\" serves as a crucial component in representing and analyzing the interconnectedness of various entities and concepts related to COVID-19 within a knowledge graph framework.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'label'}]
    },
    "covid_knowledge_graph_nodes_author": {
        "columns": [
            "id",
            "label",
            "first",
            "last",
            "full_name"
        ],
        "description": "The table \"covid_knowledge_graph_nodes_author\" contains information about authors who have contributed to a knowledge graph related to COVID-19. \n\n1. id: This column stores a unique identifier for each author in the table.\n2. label: This column indicates the type of entity, which in this case is an author.\n3. first: This column stores the first name of the author.\n4. last: This column stores the last name of the author.\n5. full_name: This column stores the full name of the author by combining the first and last names.\n\nOverall, the table \"covid_knowledge_graph_nodes_author\" serves to maintain a record of authors who have participated in creating or contributing to the COVID-19 knowledge graph, providing essential information about their identities and contributions.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'label'}]
    },
    "covid_knowledge_graph_nodes_concept": {
        "columns": [
            "id",
            "label",
            "entity",
            "concept"
        ],
        "description": "The table \"covid_knowledge_graph_nodes_concept\" contains information related to concepts within the domain of COVID-19 knowledge graph. \n\n1. id: This column stores a unique identifier for each concept node in the knowledge graph.\n2. label: This column represents the label or name associated with the concept.\n3. entity: This column contains information about the entity or object that the concept represents.\n4. concept: This column stores the actual concept or idea that is being represented in the knowledge graph.\n\nOverall, this table serves as a repository for organizing and storing various concepts related to COVID-19 within a knowledge graph structure, allowing for efficient retrieval and analysis of information related to the topic.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'label'}]
    },
    "covid_knowledge_graph_nodes_institution": {
        "columns": [
            "id",
            "label",
            "institution",
            "country",
            "settlement"
        ],
        "description": "The table \"covid_knowledge_graph_nodes_institution\" contains information about institutions related to COVID-19 within a knowledge graph. \n\n- 'id': This column stores a unique identifier for each institution node in the knowledge graph.\n- 'label': This column stores the label or name of the institution.\n- 'institution': This column stores the specific institution's name or type, such as a hospital, research center, or government agency.\n- 'country': This column stores the country where the institution is located.\n- 'settlement': This column stores the specific settlement or city where the institution is situated within the country.\n\nThis table provides a structured representation of various institutions involved in COVID-19 research, response, or management within different countries and settlements. It allows for easy retrieval and analysis of information related to these institutions within the context of the knowledge graph.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'country_codes', 'column': 'country'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'label'}, {'table': 'owid_world_vaccinations', 'column': 'country'}]
    },
    "covid_knowledge_graph_nodes_paper": {
        "columns": [
            "id",
            "label",
            "doi",
            "sha_code",
            "publish_time",
            "source",
            "title",
            "year",
            "pmcid",
            "reference"
        ],
        "description": "The table \"covid_knowledge_graph_nodes_paper\" contains information related to academic papers in the context of COVID-19. Each row in the table represents a unique paper and includes the following columns:\n\n1. id: A unique identifier for each paper in the table.\n2. label: The label or category associated with the paper.\n3. doi: The Digital Object Identifier (DOI) of the paper.\n4. sha_code: The SHA code associated with the paper.\n5. publish_time: The date and time when the paper was published.\n6. source: The source or publication where the paper was published.\n7. title: The title of the paper.\n8. year: The year of publication of the paper.\n9. pmcid: The PubMed Central ID (PMCID) of the paper.\n10. reference: References cited in the paper.\n\nThis table serves as a repository of academic papers related to COVID-19, providing key metadata such as publication details, source information, title, and references. Researchers and analysts can use this table to explore and analyze the content of COVID-19 academic literature, track citations, and identify relevant papers for further study or research.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'alleninstitute_metadata', 'column': 'doi'}, {'table': 'alleninstitute_metadata', 'column': 'publish_time'}, {'table': 'alleninstitute_metadata', 'column': 'title'}, {'table': 'alleninstitute_metadata', 'column': 'pmcid'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_topic', 'column': 'label'}]
    },
    "covid_knowledge_graph_nodes_topic": {
        "columns": [
            "id",
            "label",
            "topic",
            "topic_num"
        ],
        "description": "The table \"covid_knowledge_graph_nodes_topic\" contains information related to nodes in a knowledge graph that represent topics related to COVID-19. \n\n- 'id': This column stores a unique identifier for each node in the knowledge graph.\n- 'label': This column contains the label or name of the topic represented by the node.\n- 'topic': This column provides a description or keywords related to the topic represented by the node.\n- 'topic_num': This column assigns a numerical value to each topic for classification or organization purposes within the knowledge graph.\n\nOverall, the table serves as a repository for organizing and categorizing different topics related to COVID-19 within a knowledge graph, facilitating the retrieval and analysis of information on specific subjects.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'id'}, {'table': 'county_populations', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'id'}, {'table': 'covid_knowledge_graph_edges', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_author', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_concept', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'label'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'id'}, {'table': 'covid_knowledge_graph_nodes_paper', 'column': 'label'}]
    },
    "covid_testing_states_daily": {
        "columns": [
            "date",
            "state",
            "positive",
            "negative",
            "pending",
            "hospitalized",
            "death",
            "total",
            "hash",
            "datechecked",
            "totaltestresults",
            "fips",
            "deathincrease",
            "hospitalizedincrease",
            "negativeincrease",
            "positiveincrease",
            "totaltestresultsincrease"
        ],
        "description": "The table \"covid_testing_states_daily\" contains daily data related to COVID-19 testing and outcomes at the state level. Each row in the table represents a specific date and state combination, with the following columns providing detailed information:\n\n1. date: The date for which the data is recorded.\n2. state: The state for which the data is recorded.\n3. positive: The number of positive COVID-19 cases reported.\n4. negative: The number of negative COVID-19 test results reported.\n5. pending: The number of COVID-19 tests pending results.\n6. hospitalized: The number of individuals hospitalized due to COVID-19.\n7. death: The number of deaths attributed to COVID-19.\n8. total: The total number of COVID-19 tests conducted.\n9. hash: A unique identifier for the data entry.\n10. datechecked: The date when the data was last checked or updated.\n11. totaltestresults: The total number of COVID-19 test results reported.\n12. fips: The Federal Information Processing Standards code for the state.\n13. deathincrease: The increase in the number of deaths from the previous day.\n14. hospitalizedincrease: The increase in the number of hospitalizations from the",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'aspirevc_crowd_tracing_zipcode_3digits', 'column': 'state'}, {'table': 'county_populations', 'column': 'state'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'positive'}, {'table': 'covid_testing_us_daily', 'column': 'negative'}, {'table': 'covid_testing_us_daily', 'column': 'pending'}, {'table': 'covid_testing_us_daily', 'column': 'hospitalized'}, {'table': 'covid_testing_us_daily', 'column': 'death'}, {'table': 'covid_testing_us_daily', 'column': 'total'}, {'table': 'covid_testing_us_daily', 'column': 'hash'}, {'table': 'covid_testing_us_daily', 'column': 'datechecked'}, {'table': 'covid_testing_us_daily', 'column': 'totaltestresults'}, {'table': 'covid_testing_us_daily', 'column': 'deathincrease'}, {'table': 'covid_testing_us_daily', 'column': 'hospitalizedincrease'}, {'table': 'covid_testing_us_daily', 'column': 'negativeincrease'}, {'table': 'covid_testing_us_daily', 'column': 'positiveincrease'}, {'table': 'covid_testing_us_daily', 'column': 'totaltestresultsincrease'}, {'table': 'covid_testing_us_total', 'column': 'positive'}, {'table': 'covid_testing_us_total', 'column': 'negative'}, {'table': 'covid_testing_us_total', 'column': 'hospitalized'}, {'table': 'covid_testing_us_total', 'column': 'death'}, {'table': 'covid_testing_us_total', 'column': 'total'}, {'table': 'covid_testing_us_total', 'column': 'hash'}, {'table': 'covid_testing_us_total', 'column': 'totaltestresults'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'state'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'state'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'fips'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'us_state_abbreviations', 'column': 'state'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "covid_testing_us_daily": {
        "columns": [
            "date",
            "states",
            "positive",
            "negative",
            "posneg",
            "pending",
            "hospitalized",
            "death",
            "total",
            "hash",
            "datechecked",
            "totaltestresults",
            "deathincrease",
            "hospitalizedincrease",
            "negativeincrease",
            "positiveincrease",
            "totaltestresultsincrease"
        ],
        "description": "The table \"covid_testing_us_daily\" contains daily data related to COVID-19 testing in the United States. Each row represents a specific date and includes the following columns:\n\n1. date: The date for which the data is recorded.\n2. states: The number of states included in the data.\n3. positive: The number of positive COVID-19 cases reported.\n4. negative: The number of negative COVID-19 test results reported.\n5. posneg: The sum of positive and negative COVID-19 cases.\n6. pending: The number of pending COVID-19 test results.\n7. hospitalized: The number of individuals hospitalized due to COVID-19.\n8. death: The number of deaths reported due to COVID-19.\n9. total: The total number of COVID-19 cases (positive, negative, and pending).\n10. hash: A unique identifier for the data entry.\n11. datechecked: The date when the data was last checked or updated.\n12. totaltestresults: The total number of COVID-19 test results reported.\n13. deathincrease: The increase in the number of deaths compared to the previous day.\n14. hospitalizedincrease: The increase in the number of hospitalizations compared to the previous",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'positive'}, {'table': 'covid_testing_states_daily', 'column': 'negative'}, {'table': 'covid_testing_states_daily', 'column': 'pending'}, {'table': 'covid_testing_states_daily', 'column': 'hospitalized'}, {'table': 'covid_testing_states_daily', 'column': 'death'}, {'table': 'covid_testing_states_daily', 'column': 'total'}, {'table': 'covid_testing_states_daily', 'column': 'hash'}, {'table': 'covid_testing_states_daily', 'column': 'datechecked'}, {'table': 'covid_testing_states_daily', 'column': 'totaltestresults'}, {'table': 'covid_testing_states_daily', 'column': 'deathincrease'}, {'table': 'covid_testing_states_daily', 'column': 'hospitalizedincrease'}, {'table': 'covid_testing_states_daily', 'column': 'negativeincrease'}, {'table': 'covid_testing_states_daily', 'column': 'positiveincrease'}, {'table': 'covid_testing_states_daily', 'column': 'totaltestresultsincrease'}, {'table': 'covid_testing_us_total', 'column': 'positive'}, {'table': 'covid_testing_us_total', 'column': 'negative'}, {'table': 'covid_testing_us_total', 'column': 'posneg'}, {'table': 'covid_testing_us_total', 'column': 'hospitalized'}, {'table': 'covid_testing_us_total', 'column': 'death'}, {'table': 'covid_testing_us_total', 'column': 'total'}, {'table': 'covid_testing_us_total', 'column': 'hash'}, {'table': 'covid_testing_us_total', 'column': 'totaltestresults'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "covid_testing_us_total": {
        "columns": [
            "positive",
            "negative",
            "posneg",
            "hospitalized",
            "death",
            "total",
            "hash",
            "lastmodified",
            "totaltestresults",
            "notes"
        ],
        "description": "The table \"covid_testing_us_total\" contains data related to COVID-19 testing in the United States. Here is a description of each column:\n\n1. positive: Represents the total number of positive COVID-19 test results.\n2. negative: Represents the total number of negative COVID-19 test results.\n3. posneg: Represents the total number of positive and negative COVID-19 test results combined.\n4. hospitalized: Indicates the total number of individuals who have been hospitalized due to COVID-19.\n5. death: Represents the total number of deaths attributed to COVID-19.\n6. total: Represents the total number of COVID-19 tests conducted.\n7. hash: Represents a unique identifier or checksum for the data.\n8. lastmodified: Indicates the date and time when the data was last modified.\n9. totaltestresults: Represents the total number of test results (both positive and negative).\n10. notes: Provides additional notes or information related to the data in the table.",
        "joins": [{'table': 'covid_testing_states_daily', 'column': 'positive'}, {'table': 'covid_testing_states_daily', 'column': 'negative'}, {'table': 'covid_testing_states_daily', 'column': 'hospitalized'}, {'table': 'covid_testing_states_daily', 'column': 'death'}, {'table': 'covid_testing_states_daily', 'column': 'total'}, {'table': 'covid_testing_states_daily', 'column': 'hash'}, {'table': 'covid_testing_states_daily', 'column': 'totaltestresults'}, {'table': 'covid_testing_us_daily', 'column': 'positive'}, {'table': 'covid_testing_us_daily', 'column': 'negative'}, {'table': 'covid_testing_us_daily', 'column': 'posneg'}, {'table': 'covid_testing_us_daily', 'column': 'hospitalized'}, {'table': 'covid_testing_us_daily', 'column': 'death'}, {'table': 'covid_testing_us_daily', 'column': 'total'}, {'table': 'covid_testing_us_daily', 'column': 'hash'}, {'table': 'covid_testing_us_daily', 'column': 'totaltestresults'}]
    },
    "covidcast_data": {
        "columns": [
            "data_source",
            "signal",
            "geo_type",
            "time_value",
            "geo_value",
            "direction",
            "value",
            "stderr",
            "sample_size"
        ],
        "description": "The table \"covidcast_data\" contains data related to various signals or indicators of COVID-19 activity. Each record in the table represents a specific data point for a particular geographical location at a certain time. \n\nHere is a description of the columns in the table:\n\n1. data_source: This column stores the source of the data, such as a research institution, government agency, or healthcare organization.\n   \n2. signal: This column indicates the specific COVID-19 metric or signal being measured, such as cases, deaths, hospitalizations, or testing rates.\n\n3. geo_type: This column specifies the type of geographical area being represented, such as state, county, or city.\n\n4. time_value: This column represents the timestamp or date associated with the data point.\n\n5. geo_value: This column stores the geographical identifier corresponding to the location being reported, such as the name or code of a state or county.\n\n6. direction: This column indicates the trend or direction of the data point, such as increasing, decreasing, or stable.\n\n7. value: This column contains the actual value of the COVID-19 metric being measured.\n\n8. stderr: This column stores the standard error associated with the data point, providing a measure of",
        "joins": [{'table': 'covidcast_metadata', 'column': 'data_source'}, {'table': 'covidcast_metadata', 'column': 'signal'}, {'table': 'covidcast_metadata', 'column': 'geo_type'}]
    },
    "covidcast_metadata": {
        "columns": [
            "data_source",
            "signal",
            "time_type",
            "geo_type",
            "min_time",
            "max_time",
            "num_locations",
            "min_value",
            "max_value",
            "mean_value",
            "stdev_value"
        ],
        "description": "The table \"covidcast_metadata\" contains metadata information related to various COVID-19 signals collected from different data sources. \n\n- 'data_source': This column stores the name of the source providing the COVID-19 data.\n- 'signal': Represents the specific type of COVID-19 data or signal being measured.\n- 'time_type': Indicates the type of time data is being recorded, such as daily, weekly, etc.\n- 'geo_type': Specifies the geographical level at which the data is aggregated, such as country, state, county, etc.\n- 'min_time': Represents the earliest timestamp of data collection for the signal.\n- 'max_time': Represents the latest timestamp of data collection for the signal.\n- 'num_locations': Indicates the number of locations or geographical entities for which data is available.\n- 'min_value': Represents the minimum value recorded for the signal.\n- 'max_value': Represents the maximum value recorded for the signal.\n- 'mean_value': Represents the average value of the signal across all locations.\n- 'stdev_value': Represents the standard deviation of the signal values across all locations.\n\nThis table serves as a reference for understanding the characteristics and statistical summary of the COVID-19 data signals available in the database,",
        "joins": [{'table': 'covidcast_data', 'column': 'data_source'}, {'table': 'covidcast_data', 'column': 'signal'}, {'table': 'covidcast_data', 'column': 'geo_type'}]
    },
    "enigma_aggregation_global": {
        "columns": [
            "geographic_level",
            "country_name",
            "country_iso2",
            "country_iso3",
            "state_fips",
            "state_name",
            "county_fips",
            "county_name",
            "area_name",
            "lat",
            "long",
            "population",
            "date",
            "cases",
            "deaths",
            "tests",
            "tests_pending",
            "tests_negative",
            "tests_positive",
            "tests_units",
            "patients_icu",
            "patients_hosp",
            "patients_vent",
            "recovered",
            "version_timestamp"
        ],
        "description": "The table \"enigma_aggregation_global\" contains aggregated data related to the COVID-19 pandemic at various geographic levels such as country, state, and county. \n\n- 'geographic_level': Indicates the level of geography for the data (e.g., country, state, county).\n- 'country_name': Name of the country.\n- 'country_iso2': ISO 2-letter country code.\n- 'country_iso3': ISO 3-letter country code.\n- 'state_fips': FIPS code for the state.\n- 'state_name': Name of the state.\n- 'county_fips': FIPS code for the county.\n- 'county_name': Name of the county.\n- 'area_name': Name of the area.\n- 'lat': Latitude coordinate of the location.\n- 'long': Longitude coordinate of the location.\n- 'population': Population count of the geographic area.\n- 'date': Date of the data entry.\n- 'cases': Total number of confirmed cases.\n- 'deaths': Total number of deaths reported.\n- 'tests': Total number of tests conducted.\n- 'tests_pending': Number of tests pending results.\n- 'tests_negative': Number of negative test results.\n- 'tests_positive': Number of",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'country_name'}, {'table': 'enigma_aggregation_global_countries', 'column': 'country_iso2'}, {'table': 'enigma_aggregation_global_countries', 'column': 'country_iso3'}, {'table': 'enigma_aggregation_global_countries', 'column': 'lat'}, {'table': 'enigma_aggregation_global_countries', 'column': 'long'}, {'table': 'enigma_aggregation_global_countries', 'column': 'population'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_global_countries', 'column': 'tests'}, {'table': 'enigma_aggregation_global_countries', 'column': 'tests_units'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'county_fips'}, {'table': 'enigma_aggregation_us_counties', 'column': 'county_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'area_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'lat'}, {'table': 'enigma_aggregation_us_counties', 'column': 'long'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_states', 'column': 'lat'}, {'table': 'enigma_aggregation_us_states', 'column': 'long'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'tests'}, {'table': 'enigma_aggregation_us_states', 'column': 'tests_pending'}, {'table': 'enigma_aggregation_us_states', 'column': 'tests_negative'}, {'table': 'enigma_aggregation_us_states', 'column': 'tests_positive'}, {'table': 'enigma_aggregation_us_states', 'column': 'patients_icu'}, {'table': 'enigma_aggregation_us_states', 'column': 'patients_hosp'}, {'table': 'enigma_aggregation_us_states', 'column': 'patients_vent'}, {'table': 'enigma_aggregation_us_states', 'column': 'recovered'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'recovered'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'recovered'}, {'table': 'hospital_beds', 'column': 'state_fips'}, {'table': 'hospital_beds', 'column': 'state_name'}, {'table': 'hospital_beds', 'column': 'county_name'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_covid_datahub', 'column': 'county_name'}, {'table': 'tableau_jhu', 'column': 'lat'}, {'table': 'tableau_jhu', 'column': 'long'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'tests_units'}]
    },
    "enigma_aggregation_global_countries": {
        "columns": [
            "country_name",
            "country_iso2",
            "country_iso3",
            "lat",
            "long",
            "population",
            "date",
            "cases",
            "deaths",
            "tests",
            "tests_units"
        ],
        "description": "The table \"enigma_aggregation_global_countries\" contains data related to the COVID-19 pandemic at a global level, specifically focusing on individual countries. \n\n1. country_name: This column stores the name of the country.\n2. country_iso2: This column contains the ISO 3166-1 alpha-2 code for the country.\n3. country_iso3: This column contains the ISO 3166-1 alpha-3 code for the country.\n4. lat: This column stores the latitude coordinate of the country.\n5. long: This column stores the longitude coordinate of the country.\n6. population: This column contains the population count of the country.\n7. date: This column stores the date for which the data is recorded.\n8. cases: This column stores the number of confirmed COVID-19 cases in the country on a specific date.\n9. deaths: This column stores the number of COVID-19 related deaths in the country on a specific date.\n10. tests: This column stores the number of COVID-19 tests conducted in the country on a specific date.\n11. tests_units: This column specifies the units in which the number of tests is recorded (e.g., 'tests per thousand', 'tests per",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'country_name'}, {'table': 'enigma_aggregation_global', 'column': 'country_iso2'}, {'table': 'enigma_aggregation_global', 'column': 'country_iso3'}, {'table': 'enigma_aggregation_global', 'column': 'lat'}, {'table': 'enigma_aggregation_global', 'column': 'long'}, {'table': 'enigma_aggregation_global', 'column': 'population'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global', 'column': 'tests'}, {'table': 'enigma_aggregation_global', 'column': 'tests_units'}, {'table': 'enigma_aggregation_us_counties', 'column': 'lat'}, {'table': 'enigma_aggregation_us_counties', 'column': 'long'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'lat'}, {'table': 'enigma_aggregation_us_states', 'column': 'long'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'tests'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'lat'}, {'table': 'tableau_jhu', 'column': 'long'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'tests_units'}]
    },
    "enigma_aggregation_us_counties": {
        "columns": [
            "state_fips",
            "state_name",
            "county_fips",
            "county_name",
            "area_name",
            "lat",
            "long",
            "date",
            "cases",
            "deaths"
        ],
        "description": "The table \"enigma_aggregation_us_counties\" contains data related to COVID-19 cases and deaths in counties across the United States. \n\n- state_fips: The FIPS code for the state where the county is located.\n- state_name: The name of the state where the county is located.\n- county_fips: The FIPS code for the county.\n- county_name: The name of the county.\n- area_name: The name of the area within the county.\n- lat: The latitude coordinate of the county.\n- long: The longitude coordinate of the county.\n- date: The date for which the COVID-19 data is recorded.\n- cases: The number of confirmed COVID-19 cases in the county on the given date.\n- deaths: The number of COVID-19 related deaths in the county on the given date.\n\nThis table provides a detailed breakdown of COVID-19 statistics at the county level, including the number of cases and deaths, allowing for analysis and tracking of the impact of the pandemic in different regions of the United States.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'state_fips'}, {'table': 'enigma_aggregation_global', 'column': 'state_name'}, {'table': 'enigma_aggregation_global', 'column': 'county_fips'}, {'table': 'enigma_aggregation_global', 'column': 'county_name'}, {'table': 'enigma_aggregation_global', 'column': 'area_name'}, {'table': 'enigma_aggregation_global', 'column': 'lat'}, {'table': 'enigma_aggregation_global', 'column': 'long'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global_countries', 'column': 'lat'}, {'table': 'enigma_aggregation_global_countries', 'column': 'long'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_states', 'column': 'lat'}, {'table': 'enigma_aggregation_us_states', 'column': 'long'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'hospital_beds', 'column': 'state_fips'}, {'table': 'hospital_beds', 'column': 'state_name'}, {'table': 'hospital_beds', 'column': 'county_name'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_covid_datahub', 'column': 'county_name'}, {'table': 'tableau_jhu', 'column': 'lat'}, {'table': 'tableau_jhu', 'column': 'long'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "enigma_aggregation_us_states": {
        "columns": [
            "state_fips",
            "state_name",
            "lat",
            "long",
            "date",
            "cases",
            "deaths",
            "tests",
            "tests_pending",
            "tests_negative",
            "tests_positive",
            "patients_icu",
            "patients_hosp",
            "patients_vent",
            "recovered"
        ],
        "description": "The table \"enigma_aggregation_us_states\" contains data related to the COVID-19 pandemic in the United States at the state level. Each row in the table represents a specific state on a particular date and includes the following columns:\n\n1. state_fips: The FIPS code for the state.\n2. state_name: The name of the state.\n3. lat: The latitude coordinate of the state.\n4. long: The longitude coordinate of the state.\n5. date: The date for which the data is recorded.\n6. cases: The total number of confirmed COVID-19 cases in the state.\n7. deaths: The total number of COVID-19 related deaths in the state.\n8. tests: The total number of COVID-19 tests conducted in the state.\n9. tests_pending: The number of COVID-19 tests that are pending results.\n10. tests_negative: The number of COVID-19 tests with negative results.\n11. tests_positive: The number of COVID-19 tests with positive results.\n12. patients_icu: The number of COVID-19 patients in the state who are in the Intensive Care Unit (ICU).\n13. patients_hosp: The number of COVID-19 patients in the",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'state_fips'}, {'table': 'enigma_aggregation_global', 'column': 'state_name'}, {'table': 'enigma_aggregation_global', 'column': 'lat'}, {'table': 'enigma_aggregation_global', 'column': 'long'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global', 'column': 'tests'}, {'table': 'enigma_aggregation_global', 'column': 'tests_pending'}, {'table': 'enigma_aggregation_global', 'column': 'tests_negative'}, {'table': 'enigma_aggregation_global', 'column': 'tests_positive'}, {'table': 'enigma_aggregation_global', 'column': 'patients_icu'}, {'table': 'enigma_aggregation_global', 'column': 'patients_hosp'}, {'table': 'enigma_aggregation_global', 'column': 'patients_vent'}, {'table': 'enigma_aggregation_global', 'column': 'recovered'}, {'table': 'enigma_aggregation_global_countries', 'column': 'lat'}, {'table': 'enigma_aggregation_global_countries', 'column': 'long'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_global_countries', 'column': 'tests'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'lat'}, {'table': 'enigma_aggregation_us_counties', 'column': 'long'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'recovered'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'recovered'}, {'table': 'hospital_beds', 'column': 'state_fips'}, {'table': 'hospital_beds', 'column': 'state_name'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'lat'}, {'table': 'tableau_jhu', 'column': 'long'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "enigma_jhu": {
        "columns": [
            "fips",
            "admin2",
            "province_state",
            "country_region",
            "last_update",
            "latitude",
            "longitude",
            "confirmed",
            "deaths",
            "recovered",
            "active",
            "combined_key"
        ],
        "description": "The table \"enigma_jhu\" contains data related to the COVID-19 pandemic, specifically tracking cases and outcomes at a regional level. \n\n1. fips: The FIPS code for the location.\n2. admin2: The administrative area within the region.\n3. province_state: The province or state within the country.\n4. country_region: The country or region where the data is recorded.\n5. last_update: The date and time of the last update for the data entry.\n6. latitude: The latitude coordinate of the location.\n7. longitude: The longitude coordinate of the location.\n8. confirmed: The number of confirmed COVID-19 cases in the specified region.\n9. deaths: The number of deaths due to COVID-19 in the specified region.\n10. recovered: The number of individuals who have recovered from COVID-19 in the specified region.\n11. active: The number of currently active COVID-19 cases in the specified region.\n12. combined_key: A combined key that uniquely identifies the location.\n\nThis table serves as a comprehensive dataset for tracking and analyzing the spread and impact of COVID-19 across different regions, providing valuable insights for public health officials, researchers, and policymakers.",
        "joins": [{'table': 'country_codes', 'column': 'latitude'}, {'table': 'country_codes', 'column': 'longitude'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global', 'column': 'recovered'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'recovered'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'admin2'}, {'table': 'enigma_jhu_timeseries', 'column': 'province_state'}, {'table': 'enigma_jhu_timeseries', 'column': 'country_region'}, {'table': 'enigma_jhu_timeseries', 'column': 'latitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'longitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'confirmed'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'recovered'}, {'table': 'enigma_jhu_timeseries', 'column': 'active'}, {'table': 'enigma_jhu_timeseries', 'column': 'combined_key'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'hospital_beds', 'column': 'latitude'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'prediction_models_severity_index', 'column': 'latitude'}, {'table': 'prediction_models_severity_index', 'column': 'longitude'}, {'table': 'tableau_jhu', 'column': 'fips'}, {'table': 'tableau_jhu', 'column': 'admin2'}, {'table': 'tableau_jhu', 'column': 'province_state'}, {'table': 'tableau_jhu', 'column': 'country_region'}, {'table': 'tableau_jhu', 'column': 'combined_key'}]
    },
    "enigma_jhu_timeseries": {
        "columns": [
            "uid",
            "fips",
            "iso2",
            "iso3",
            "code3",
            "admin2",
            "latitude",
            "longitude",
            "province_state",
            "country_region",
            "date",
            "confirmed",
            "deaths",
            "recovered",
            "active",
            "combined_key"
        ],
        "description": "The table \"enigma_jhu_timeseries\" contains time-series data related to the COVID-19 pandemic. Each row in the table represents a specific instance of data recorded for a particular location and date. \n\n- 'uid': Unique identifier for each record.\n- 'fips': Federal Information Processing Standards code for the location.\n- 'iso2': ISO 3166-1 alpha-2 code for the country.\n- 'iso3': ISO 3166-1 alpha-3 code for the country.\n- 'code3': Numeric code for the country.\n- 'admin2': Administrative division level 2 within the country.\n- 'latitude': Latitude coordinate of the location.\n- 'longitude': Longitude coordinate of the location.\n- 'province_state': Province or state within the country.\n- 'country_region': Country or region name.\n- 'date': Date for which the data is recorded.\n- 'confirmed': Number of confirmed COVID-19 cases.\n- 'deaths': Number of deaths due to COVID-19.\n- 'recovered': Number of recovered cases from COVID-19.\n- 'active': Number of active cases at the time of recording.\n- 'combined_key': Combined key of the location including province/state",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'country_codes', 'column': 'latitude'}, {'table': 'country_codes', 'column': 'longitude'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global', 'column': 'recovered'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'recovered'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu', 'column': 'admin2'}, {'table': 'enigma_jhu', 'column': 'latitude'}, {'table': 'enigma_jhu', 'column': 'longitude'}, {'table': 'enigma_jhu', 'column': 'province_state'}, {'table': 'enigma_jhu', 'column': 'country_region'}, {'table': 'enigma_jhu', 'column': 'confirmed'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'recovered'}, {'table': 'enigma_jhu', 'column': 'active'}, {'table': 'enigma_jhu', 'column': 'combined_key'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'hospital_beds', 'column': 'latitude'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'prediction_models_severity_index', 'column': 'latitude'}, {'table': 'prediction_models_severity_index', 'column': 'longitude'}, {'table': 'tableau_jhu', 'column': 'fips'}, {'table': 'tableau_jhu', 'column': 'admin2'}, {'table': 'tableau_jhu', 'column': 'province_state'}, {'table': 'tableau_jhu', 'column': 'country_region'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'combined_key'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "hospital_beds": {
        "columns": [
            "objectid",
            "hospital_name",
            "hospital_type",
            "hq_address",
            "hq_address1",
            "hq_city",
            "hq_state",
            "hq_zip_code",
            "county_name",
            "state_name",
            "state_fips",
            "cnty_fips",
            "fips",
            "num_licensed_beds",
            "num_staffed_beds",
            "num_icu_beds",
            "bed_utilization",
            "potential_increase_in_bed_capac",
            "latitude",
            "longtitude"
        ],
        "description": "The table \"hospital_beds\" contains information related to hospital bed capacity in various healthcare facilities. Each row in the table represents a specific hospital and includes details such as the hospital name, type, address, county, state, and geographic coordinates. \n\nThe columns in the table are as follows:\n\n1. objectid: A unique identifier for each record in the table.\n2. hospital_name: The name of the hospital.\n3. hospital_type: The type of hospital (e.g., general, specialty, etc.).\n4. hq_address: The headquarters address of the hospital.\n5. hq_address1: Additional address information for the hospital headquarters.\n6. hq_city: The city where the hospital headquarters is located.\n7. hq_state: The state where the hospital headquarters is located.\n8. hq_zip_code: The ZIP code of the hospital headquarters.\n9. county_name: The name of the county where the hospital is located.\n10. state_name: The name of the state where the hospital is located.\n11. state_fips: The Federal Information Processing Standards (FIPS) code for the state.\n12. cnty_fips: The FIPS code for the county.\n13. fips:",
        "joins": [{'table': 'country_codes', 'column': 'latitude'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'enigma_aggregation_global', 'column': 'county_name'}, {'table': 'enigma_aggregation_global', 'column': 'state_name'}, {'table': 'enigma_aggregation_global', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_counties', 'column': 'county_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'state_fips'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_name'}, {'table': 'enigma_aggregation_us_states', 'column': 'state_fips'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu', 'column': 'latitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'latitude'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'prediction_models_severity_index', 'column': 'hospital_name'}, {'table': 'prediction_models_severity_index', 'column': 'latitude'}, {'table': 'tableau_covid_datahub', 'column': 'county_name'}, {'table': 'tableau_jhu', 'column': 'fips'}]
    },
    "nytimes_counties": {
        "columns": [
            "date",
            "county",
            "state",
            "fips",
            "cases",
            "deaths"
        ],
        "description": "The table \"nytimes_counties\" contains data related to COVID-19 cases and deaths in various counties across different states. \n\n- 'date': This column stores the date when the data was recorded, providing a time reference for the reported cases and deaths.\n- 'county': This column specifies the name of the county where the COVID-19 cases and deaths occurred.\n- 'state': This column indicates the state to which the county belongs, providing geographical context for the data.\n- 'fips': This column contains the Federal Information Processing Standards (FIPS) code for the county, which is a unique identifier used for geographic areas.\n- 'cases': This column records the number of confirmed COVID-19 cases reported in the respective county on the given date.\n- 'deaths': This column captures the number of deaths due to COVID-19 reported in the respective county on the given date.\n\nOverall, the table \"nytimes_counties\" serves as a repository for tracking and analyzing COVID-19 data at the county level, enabling researchers, policymakers, and the public to monitor the spread and impact of the virus in specific geographic areas.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'aspirevc_crowd_tracing_zipcode_3digits', 'column': 'state'}, {'table': 'county_populations', 'column': 'county'}, {'table': 'county_populations', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'state'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'fips'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'us_state_abbreviations', 'column': 'state'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "nytimes_states": {
        "columns": [
            "date",
            "state",
            "fips",
            "cases",
            "deaths"
        ],
        "description": "The table \"nytimes_states\" contains data related to COVID-19 cases and deaths in different states of the United States. \n\n1. 'date': This column represents the date when the data was recorded or reported.\n2. 'state': This column indicates the name of the state for which the COVID-19 data is being reported.\n3. 'fips': This column contains the Federal Information Processing Standards (FIPS) code for the state, which is a unique identifier assigned to each state.\n4. 'cases': This column shows the total number of confirmed COVID-19 cases reported in the respective state on the given date.\n5. 'deaths': This column displays the total number of deaths due to COVID-19 reported in the respective state on the given date.\n\nOverall, the table \"nytimes_states\" provides a detailed record of COVID-19 cases and deaths by state, allowing for analysis and tracking of the pandemic's impact across different regions of the United States over time.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'aspirevc_crowd_tracing_zipcode_3digits', 'column': 'state'}, {'table': 'county_populations', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'deaths'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'deaths'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'deaths'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu', 'column': 'deaths'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'deaths'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'state'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'deaths'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'fips'}, {'table': 'tableau_jhu', 'column': 'cases'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'us_state_abbreviations', 'column': 'state'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "owid_us_state_vaccinations": {
        "columns": [
            "location",
            "date",
            "total_vaccinations",
            "total_vaccinations_per_hundred",
            "daily_vaccinations_raw",
            "daily_vaccinations",
            "daily_vaccinations_per_million",
            "people_vaccinated",
            "people_vaccinated_per_hundred",
            "people_fully_vaccinated",
            "people_fully_vaccinated_per_hundred",
            "total_distributed",
            "total_distributed_per_hundred",
            "share_doses_used"
        ],
        "description": "The table \"owid_us_state_vaccinations\" contains data related to COVID-19 vaccinations in different states of the United States. Each row in the table represents a specific state on a particular date and includes the following columns:\n\n1. location: The name of the state where the data was recorded.\n2. date: The date when the data was reported.\n3. total_vaccinations: The total number of COVID-19 vaccine doses administered in the state.\n4. total_vaccinations_per_hundred: The total number of COVID-19 vaccine doses administered per hundred people in the state.\n5. daily_vaccinations_raw: The number of COVID-19 vaccine doses administered on a specific day without any smoothing or adjustment.\n6. daily_vaccinations: The number of COVID-19 vaccine doses administered on a specific day, possibly adjusted or smoothed.\n7. daily_vaccinations_per_million: The number of COVID-19 vaccine doses administered per million people on a specific day.\n8. people_vaccinated: The total number of individuals who have received at least one dose of the COVID-19 vaccine.\n9. people_vaccinated_per_hundred: The percentage of people in the state who have received at least one",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'total_vaccinations'}, {'table': 'owid_world_vaccinations', 'column': 'total_vaccinations_per_hundred'}, {'table': 'owid_world_vaccinations', 'column': 'daily_vaccinations_raw'}, {'table': 'owid_world_vaccinations', 'column': 'daily_vaccinations'}, {'table': 'owid_world_vaccinations', 'column': 'daily_vaccinations_per_million'}, {'table': 'owid_world_vaccinations', 'column': 'people_vaccinated'}, {'table': 'owid_world_vaccinations', 'column': 'people_vaccinated_per_hundred'}, {'table': 'owid_world_vaccinations', 'column': 'people_fully_vaccinated'}, {'table': 'owid_world_vaccinations', 'column': 'people_fully_vaccinated_per_hundred'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'location'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'total_vaccinations'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'location'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "owid_world_vaccinations": {
        "columns": [
            "country",
            "iso_code",
            "date",
            "total_vaccinations",
            "total_vaccinations_per_hundred",
            "daily_vaccinations_raw",
            "daily_vaccinations",
            "daily_vaccinations_per_million",
            "people_vaccinated",
            "people_vaccinated_per_hundred",
            "people_fully_vaccinated",
            "people_fully_vaccinated_per_hundred"
        ],
        "description": "The table \"owid_world_vaccinations\" contains data related to COVID-19 vaccinations on a global scale. It includes the following columns:\n\n1. 'country': Represents the name of the country where the data was recorded.\n2. 'iso_code': Represents the ISO code of the country for standardization and identification purposes.\n3. 'date': Represents the date when the data was recorded.\n4. 'total_vaccinations': Indicates the total number of COVID-19 vaccine doses administered in the country up to the given date.\n5. 'total_vaccinations_per_hundred': Represents the total number of COVID-19 vaccine doses administered per hundred people in the country.\n6. 'daily_vaccinations_raw': Represents the daily change in the total number of COVID-19 vaccine doses administered.\n7. 'daily_vaccinations': Indicates the number of COVID-19 vaccine doses administered on the given date.\n8. 'daily_vaccinations_per_million': Represents the number of COVID-19 vaccine doses administered per million people on the given date.\n9. 'people_vaccinated': Indicates the total number of individuals who received at least one dose of the COVID-19 vaccine.\n10. 'people_vaccinated_per_h",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'country_codes', 'column': 'country'}, {'table': 'covid_knowledge_graph_nodes_institution', 'column': 'country'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'total_vaccinations'}, {'table': 'owid_us_state_vaccinations', 'column': 'total_vaccinations_per_hundred'}, {'table': 'owid_us_state_vaccinations', 'column': 'daily_vaccinations_raw'}, {'table': 'owid_us_state_vaccinations', 'column': 'daily_vaccinations'}, {'table': 'owid_us_state_vaccinations', 'column': 'daily_vaccinations_per_million'}, {'table': 'owid_us_state_vaccinations', 'column': 'people_vaccinated'}, {'table': 'owid_us_state_vaccinations', 'column': 'people_vaccinated_per_hundred'}, {'table': 'owid_us_state_vaccinations', 'column': 'people_fully_vaccinated'}, {'table': 'owid_us_state_vaccinations', 'column': 'people_fully_vaccinated_per_hundred'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'total_vaccinations'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'iso_code'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "owid_world_vaccinations_by_manufacturer": {
        "columns": [
            "location",
            "date",
            "vaccine",
            "total_vaccinations"
        ],
        "description": "The table \"owid_world_vaccinations_by_manufacturer\" contains data related to COVID-19 vaccinations administered worldwide, categorized by the manufacturer of the vaccine. \n\n- 'location': This column indicates the geographical location where the vaccinations were administered.\n- 'date': This column represents the date on which the vaccinations were administered.\n- 'vaccine': This column specifies the manufacturer of the COVID-19 vaccine used for the vaccinations.\n- 'total_vaccinations': This column shows the total number of vaccinations administered for each specific vaccine manufacturer on a particular date in a given location.\n\nBy organizing data in this table, it allows for tracking and analyzing the distribution and administration of COVID-19 vaccines globally, with a focus on different vaccine manufacturers. This information can be valuable for monitoring vaccination progress, identifying trends, and making informed decisions related to public health strategies and vaccine distribution efforts.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'location'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'total_vaccinations'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'total_vaccinations'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'location'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "prediction_models_county_predictions": {
        "columns": [
            "countyfips",
            "countyname",
            "statename",
            "severity_county_5-day",
            "predicted_date",
            "predicted_deaths"
        ],
        "description": "The table \"prediction_models_county_predictions\" contains predictions for the number of deaths in different counties within a state. It includes the following columns:\n\n1. countyfips: The FIPS code that uniquely identifies each county.\n2. countyname: The name of the county for which the prediction is made.\n3. statename: The name of the state to which the county belongs.\n4. severity_county_5-day: A measure of the severity of the predicted impact on the county over a 5-day period.\n5. predicted_date: The date for which the prediction is made.\n6. predicted_deaths: The predicted number of deaths in the county on the specified date.\n\nThis table is designed to store and manage predictions generated by various models for different counties, allowing for the tracking and analysis of predicted death rates in response to specific events or conditions.",
        "joins": [{'table': 'prediction_models_severity_index', 'column': 'countyfips'}, {'table': 'prediction_models_severity_index', 'column': 'countyname'}, {'table': 'prediction_models_severity_index', 'column': 'statename'}]
    },
    "prediction_models_severity_index": {
        "columns": [
            "severity_1-day",
            "severity_2-day",
            "severity_3-day",
            "severity_4-day",
            "severity_5-day",
            "severity_6-day",
            "severity_7-day",
            "total_deaths_hospital",
            "hospital_name",
            "cms_certification_number",
            "countyfips",
            "countyname",
            "statename",
            "system_affiliation",
            "latitude",
            "longitude"
        ],
        "description": "The table \"prediction_models_severity_index\" contains data related to the severity index predictions for different time frames (1-day to 7-day) for a specific hospital. It also includes information about the total number of deaths in the hospital, the hospital's name, CMS certification number, county FIPS code, county name, state name, system affiliation, latitude, and longitude coordinates.\n\nThis table is designed to store and track the severity index predictions for different time periods, along with key information about the hospital such as location, certification details, and system affiliation. The severity index predictions provide insights into the expected severity of cases in the hospital over the specified time frames, aiding in resource allocation, staffing decisions, and overall preparedness for potential outcomes. The additional hospital details and geographic information allow for further analysis and correlation with external datasets for a comprehensive understanding of the healthcare landscape.",
        "joins": [{'table': 'country_codes', 'column': 'latitude'}, {'table': 'country_codes', 'column': 'longitude'}, {'table': 'enigma_jhu', 'column': 'latitude'}, {'table': 'enigma_jhu', 'column': 'longitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'latitude'}, {'table': 'enigma_jhu_timeseries', 'column': 'longitude'}, {'table': 'hospital_beds', 'column': 'hospital_name'}, {'table': 'hospital_beds', 'column': 'latitude'}, {'table': 'prediction_models_county_predictions', 'column': 'countyfips'}, {'table': 'prediction_models_county_predictions', 'column': 'countyname'}, {'table': 'prediction_models_county_predictions', 'column': 'statename'}]
    },
    "tableau_covid_datahub": {
        "columns": [
            "country_short_name",
            "country_alpha_3_code",
            "country_alpha_2_code",
            "continent_name",
            "province_state_name",
            "county_name",
            "county_fips_number",
            "people_positive_cases_count",
            "report_date",
            "data_source_name",
            "people_death_new_count",
            "people_positive_new_cases_count",
            "people_death_count"
        ],
        "description": "The table \"tableau_covid_datahub\" contains data related to COVID-19 cases and deaths at various geographical levels. Here is a description of each column:\n\n1. country_short_name: The short name or abbreviation of the country.\n2. country_alpha_3_code: The three-letter country code as per the ISO 3166 standard.\n3. country_alpha_2_code: The two-letter country code as per the ISO 3166 standard.\n4. continent_name: The name of the continent where the country is located.\n5. province_state_name: The name of the province or state within the country.\n6. county_name: The name of the county or region within the province/state.\n7. county_fips_number: The FIPS (Federal Information Processing Standards) code for the county.\n8. people_positive_cases_count: The total count of people who tested positive for COVID-19.\n9. report_date: The date when the data was reported.\n10. data_source_name: The name of the source providing the data.\n11. people_death_new_count: The count of new deaths reported on the given date.\n12. people_positive_new_cases_count: The count of new positive cases reported on the given date.\n13",
        "joins": [{'table': 'enigma_aggregation_global', 'column': 'county_name'}, {'table': 'enigma_aggregation_us_counties', 'column': 'county_name'}, {'table': 'hospital_beds', 'column': 'county_name'}]
    },
    "tableau_jhu": {
        "columns": [
            "case_type",
            "cases",
            "difference",
            "date",
            "country_region",
            "province_state",
            "admin2",
            "combined_key",
            "fips",
            "lat",
            "long",
            "table_names",
            "prep_flow_runtime"
        ],
        "description": "The \"tableau_jhu\" table contains data related to COVID-19 cases reported in various regions. \n\n- case_type: Indicates the type of case (e.g., confirmed, deaths, recovered).\n- cases: Represents the number of cases reported for a specific case type.\n- difference: Represents the difference in cases compared to the previous date.\n- date: Represents the date for which the data is recorded.\n- country_region: Indicates the country or region where the cases are reported.\n- province_state: Represents the province or state within the country or region.\n- admin2: Represents administrative divisions within the province or state.\n- combined_key: Provides a combined key for the location, including country/region, province/state, and admin2.\n- fips: Federal Information Processing Standards code for the location.\n- lat: Latitude coordinate of the location.\n- long: Longitude coordinate of the location.\n- table_names: Indicates the source or table name from where the data is extracted.\n- prep_flow_runtime: Represents the runtime for data preparation flow.\n\nOverall, this table serves as a comprehensive repository of COVID-19 case data, including details on case types, locations, dates, and data preparation information.",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'fips'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'cases'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'lat'}, {'table': 'enigma_aggregation_global', 'column': 'long'}, {'table': 'enigma_aggregation_global_countries', 'column': 'cases'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'lat'}, {'table': 'enigma_aggregation_global_countries', 'column': 'long'}, {'table': 'enigma_aggregation_us_counties', 'column': 'cases'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'lat'}, {'table': 'enigma_aggregation_us_counties', 'column': 'long'}, {'table': 'enigma_aggregation_us_states', 'column': 'cases'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'lat'}, {'table': 'enigma_aggregation_us_states', 'column': 'long'}, {'table': 'enigma_jhu', 'column': 'country_region'}, {'table': 'enigma_jhu', 'column': 'province_state'}, {'table': 'enigma_jhu', 'column': 'admin2'}, {'table': 'enigma_jhu', 'column': 'combined_key'}, {'table': 'enigma_jhu', 'column': 'fips'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'country_region'}, {'table': 'enigma_jhu_timeseries', 'column': 'province_state'}, {'table': 'enigma_jhu_timeseries', 'column': 'admin2'}, {'table': 'enigma_jhu_timeseries', 'column': 'combined_key'}, {'table': 'enigma_jhu_timeseries', 'column': 'fips'}, {'table': 'hospital_beds', 'column': 'fips'}, {'table': 'nytimes_counties', 'column': 'cases'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'fips'}, {'table': 'nytimes_states', 'column': 'cases'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'fips'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "uk_covid": {
        "columns": [
            "areatype",
            "areaname",
            "areacode",
            "date",
            "newcasesbypublishdate",
            "cumcasesbypublishdate",
            "newcasesbyspecimendate",
            "cumcasesbyspecimendate",
            "malecases",
            "femalecases",
            "newpillaronetestsbypublishdate",
            "cumpillaronetestsbypublishdate",
            "newpillartwotestsbypublishdate",
            "cumpillartwotestsbypublishdate",
            "newpillarthreetestsbypublishdate",
            "cumpillarthreetestsbypublishdate",
            "newpillarfourtestsbypublishdate",
            "cumpillarfourtestsbypublishdate",
            "newadmissions",
            "cumadmissions",
            "cumadmissionsbyage",
            "cumtestsbypublishdate",
            "newtestsbypublishdate",
            "covidoccupiedmvbeds",
            "hospitalcases",
            "plannedcapacitybypublishdate",
            "newdeaths28daysbypublishdate",
            "cumdeaths28daysbypublishdate",
            "cumdeaths28daysbypublishdaterate",
            "newdeaths28daysbydeathdate",
            "cumdeaths28daysbydeathdate",
            "cumdeaths28daysbydeathdaterate"
        ],
        "description": "The \"uk_covid\" table contains data related to COVID-19 cases, admissions, tests, deaths, and hospital capacity in the UK. \n\n- 'areatype': Type of area (e.g., region, local authority).\n- 'areaname': Name of the specific area.\n- 'areacode': Code assigned to the area.\n- 'date': Date of the data entry.\n- 'newcasesbypublishdate': Number of new cases reported on the publishing date.\n- 'cumcasesbypublishdate': Cumulative number of cases reported by the publishing date.\n- 'newcasesbyspecimendate': Number of new cases based on specimen date.\n- 'cumcasesbyspecimendate': Cumulative number of cases based on specimen date.\n- 'malecases': Number of cases reported among males.\n- 'femalecases': Number of cases reported among females.\n- 'newpillaronetestsbypublishdate': Number of new tests under pillar one reported by the publishing date.\n- 'cumpillaronetestsbypublishdate': Cumulative number of tests under pillar one reported by the publishing date.\n- 'newpillartwotestsbypublishdate': Number of new",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'world_cases_deaths_testing', 'column': 'date'}]
    },
    "us_state_abbreviations": {
        "columns": [
            "state",
            "abbreviation"
        ],
        "description": "The table \"us_state_abbreviations\" contains two columns: 'state' and 'abbreviation'.\n\nThe 'state' column stores the full names of the states in the United States, while the 'abbreviation' column stores the corresponding two-letter abbreviations for each state. This table serves as a reference for mapping the full state names to their respective abbreviations, which is commonly used in various applications and systems for data processing and presentation purposes.\n\nBy providing a standardized and consistent mapping between state names and abbreviations, this table facilitates data integration, analysis, and reporting tasks that involve state-related information. It simplifies the process of identifying and referencing states within datasets, reports, and applications by using the standardized two-letter abbreviations.",
        "joins": [{'table': 'aspirevc_crowd_tracing_zipcode_3digits', 'column': 'state'}, {'table': 'county_populations', 'column': 'state'}, {'table': 'covid_testing_states_daily', 'column': 'state'}, {'table': 'nytimes_counties', 'column': 'state'}, {'table': 'nytimes_states', 'column': 'state'}]
    },
    "world_cases_deaths_testing": {
        "columns": [
            "iso_code",
            "location",
            "date",
            "total_cases",
            "new_cases",
            "total_deaths",
            "new_deaths",
            "total_cases_per_million",
            "new_cases_per_million",
            "total_deaths_per_million",
            "new_deaths_per_million",
            "total_tests",
            "new_tests",
            "total_tests_per_thousand",
            "new_tests_per_thousand",
            "tests_units"
        ],
        "description": "The table \"world_cases_deaths_testing\" contains data related to COVID-19 cases, deaths, and testing on a global scale. Each row in the table represents a specific location on a given date and includes the following columns:\n\n1. iso_code: The unique code assigned to each country or region.\n2. location: The name of the country or region.\n3. date: The date for which the data is recorded.\n...",
        "joins": [{'table': 'alleninstitute_comprehend_medical', 'column': 'date'}, {'table': 'covid_testing_states_daily', 'column': 'date'}, {'table': 'covid_testing_us_daily', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'date'}, {'table': 'enigma_aggregation_global', 'column': 'tests_units'}, {'table': 'enigma_aggregation_global_countries', 'column': 'date'}, {'table': 'enigma_aggregation_global_countries', 'column': 'tests_units'}, {'table': 'enigma_aggregation_us_counties', 'column': 'date'}, {'table': 'enigma_aggregation_us_states', 'column': 'date'}, {'table': 'enigma_jhu_timeseries', 'column': 'date'}, {'table': 'nytimes_counties', 'column': 'date'}, {'table': 'nytimes_states', 'column': 'date'}, {'table': 'owid_us_state_vaccinations', 'column': 'location'}, {'table': 'owid_us_state_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations', 'column': 'iso_code'}, {'table': 'owid_world_vaccinations', 'column': 'date'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'location'}, {'table': 'owid_world_vaccinations_by_manufacturer', 'column': 'date'}, {'table': 'tableau_jhu', 'column': 'date'}, {'table': 'uk_covid', 'column': 'date'}]
    }
}
