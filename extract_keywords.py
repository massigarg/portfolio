from keybert import KeyBERT

keywords_candidates_filtered = [
    'Politics and Government',
    'Global Warming',
    'United Nations',
    'Johnson, Boris',
    'Great Britain',
    'Coronavirus (2019-nCoV)',
    'Quarantine (Life and Culture)',
    'Putin, Vladimir V',
    'Travel and Vacations',
    'Quarantines',
    'Deaths (Fatalities)',
    'Vaccination and Immunization',
    'Demonstrations, Protests and Riots',
    'Muslims and Islam',
    'Terrorism',
    'Defense and Military Forces',
    'Human Rights and Human Rights Violations',
    'Mexico',
    'United States International Relations',
    'United States Politics and Government',
    'Biden, Joseph R Jr',
    'Palestinians',
    'Gaza Strip',
    'Israel',
    'Hamas',
    'Economic Conditions and Trends',
    'China',
    'Social Media',
    'Communist Party of China',
    'Law and Legislation',
    'Shortages',
    'Floods',
    'Civilian Casualties',
    'Afghanistan War (2001- )',
    'Hospitals',
    'Taliban',
    'AFGHANISTAN',
    'Kabul (Afghanistan)',
    'Brazil',
    'War and Armed Conflicts',
    'Refugees and Displaced Persons',
    'Russia',
    'International Relations',
    'Australia',
    'Sex Crimes',
    'South Korea',
    'War Crimes, Genocide and Crimes Against Humanity',
    'World Health Organization',
    'India',
    'Embargoes and Sanctions',
    'United States Defense and Military Forces',
    'Iran',
    'Legislatures and Parliaments',
    'Disease Rates',
    'Italy',
    'Germany',
    'Merkel, Angela',
    'Europe',
    'Elections',
    'Great Britain Withdrawal from EU (Brexit)',
    'International Trade and World Market',
    'European Union',
    'Macron, Emmanuel (1977- )',
    'France',
    'Corruption (Institutional)',
    'Canada',
    'Women and Girls',
    'Immigration and Emigration',
    'Discrimination',
    'Content Type: Personal Profile',
    'Japan',
    'Shutdowns (Institutional)',
    "Coups D'Etat and Attempted Coups D'Etat",
    'Modi, Narendra',
    'Roman Catholic Church',
    'Political Prisoners',
    'Assassinations and Attempted Assassinations',
    'Myanmar',
    'Evacuations and Evacuees',
    'Murders, Attempted Murders and Homicides',
    'News and News Media',
    'Coronavirus Reopenings',
    'United States',
    'London (England)',
    'England',
    'Belarus',
    'Poland',
    'Pfizer Inc',
    'Trump, Donald J',
    'Freedom of the Press',
    'Hong Kong',
    'Islamic State in Iraq and Syria (ISIS)',
    'Royal Families',
    'AFRICA',
    'Navalny, Aleksei A',
    'Haiti',
    'Netanyahu, Benjamin',
    "Women's Rights",
    'AstraZeneca PLC',
    'Afghan National Security Forces',
    'Francis',
    'Hong Kong Protests (2019)',
    'internal-essential']

text = 'The Biden administration plans to require most foreign visitors to be vaccinated.Biden Plans New Policy Requiring That All Foreign Travelers to U.S. Be VaccinatedThe Biden administration is developing plans to require all foreign travelers to the United States to be vaccinated against Covid-19, with limited exceptions, according to an administration official with knowledge of the developing policy.Officials say the new policy is being readied in the event that the United States eases its travel rules, which isn’t expected soon.'

# let's define the keyword extraction function


def keyword_extractor(text, top_n, diversity, mmr):
    """
    This function extracts keywords from text using KeyBERT

    It ueses a list keywords candidates where to chose from.
    Maximal Marginal Relevance (MMR) set to True
    Diversity is set to 0.2
    Top n keywords/keyphrases is set to 6

    Args:
        text (str): text to porcess

    Returns:
        list: list of keywords
    """

    kw_model = KeyBERT()

    keywords = kw_model.extract_keywords(
        text, keyphrase_ngram_range=(1, 1),
        stop_words="english",
        candidates=keywords_candidates_filtered,
        use_mmr=mmr,
        diversity=diversity,
        top_n=top_n
    )

    return str([i[0] for i in keywords])


# keyword_extractor(text, 6, 0.2, True)


if __name__ == "__main__":
    keyword_extractor(text, top_n, diversity, mmr)
# print("Extracting keywords from following text : \n", text)
# print("Extracted keywords: \n", keyword_extractor(text))
