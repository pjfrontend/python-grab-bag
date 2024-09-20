const fs = require("fs");
const wcc = require("world-countries-capitals");
const csvToJson = require("convert-csv-to-json");
const countriesPop = require("./countries_pop.json");

const getContinent = (str) => {
  switch (str) {
    case "oc":
      return ["Oceania"];
    case "na":
      return ["North America"];
    case "sa":
      return ["South America"];
    case "as":
      return ["Asia"];
    case "eu":
      return ["Europe"];
    case "af":
      return ["Africa"];
    case "eu/as":
      return ["Europe", "Asia"];
    default:
      return `**** ${str} ****`;
  }
};

function capitalizeFirstLetter(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function capitalizeEachWordInString(str) {
  return str
    .split(" ")
    .map((x) => capitalizeFirstLetter(x))
    .join(" ");
}

const rawCountryList = wcc.getAllCountryDetails();
const countryList = rawCountryList.map((c) => {
  //   for (const c of rawCountryList) {
  //     console.log(c);
  //   }
  const sanitisedCountry = c.country
    .replace("equitorial", "equatorial")
    .replace("papa", "papua");
  return {
    country: capitalizeEachWordInString(sanitisedCountry),
    // capital_s: c.capital
    //   .split(",")
    //   .map((x) => capitalizeEachWordInString(x.trim())),
    areaKm2: c.area.km2,
    areaMi2: c.area.mi2,
    // continents: getContinent(c.continent),
    // languages: c.native_language.map((x) => capitalizeEachWordInString(x)),
    // currency: capitalizeEachWordInString(c.currency),
    // famous_for: capitalizeEachWordInString(c.famous_for),
    // is_landlocked: c.is_landlocked,
  };
});

const getCountriesAreaKm2 = () => {
  function compare(a, b) {
    if (a.areaKm2 < b.areaKm2) {
      return -1;
    }
    if (a.areaKm2 > b.areaKm2) {
      return 1;
    }
    return 0;
  }
  countryList.sort(compare);
  let data = "data = [\n";
  for (const c of countryList) {
    data += `("${c.country}", ${c.areaKm2}),\n`;
  }
  data += "]";
  return data;
};

fs.writeFile(`../countries_area_km2.py`, getCountriesAreaKm2(), (err) => {
  if (err) throw err;
  console.log(`countries_area_km2.py written`);
});

const getCountriesAreaMi2 = () => {
  function compare(a, b) {
    if (a.areaMi2 < b.areaMi2) {
      return -1;
    }
    if (a.areaMi2 > b.areaMi2) {
      return 1;
    }
    return 0;
  }
  countryList.sort(compare);
  let data = "data = [\n";
  for (const c of countryList) {
    data += `("${c.country}", ${c.areaMi2}),\n`;
  }
  data += "]";
  return data;
};

fs.writeFile(`../countries_area_mi2.py`, getCountriesAreaMi2(), (err) => {
  if (err) throw err;
  console.log(`countries_area_mi2.py written`);
});

const csvFilePath = "countries_pop.csv";
let fileOutputName = "countries_pop.json";

csvToJson.generateJsonFileFromCsv(csvFilePath, fileOutputName);

// EXAMPLE
// {
//     '#': '234',
//     'Country(ordependency)': 'Holy See',
//     'Population(2023)': '518',
//     YearlyChange: '1.57 %',
//     NetChange: '8',
//     'Density(P/Km²)': '1295',
//     'LandArea(Km²)': '0',
//     'Migrants(net)': '0',
//     FertilityRate: '0',
//     MedianAge: '0%',
//     'UrbanPopulation%': '0%',
//     WorldShare: 'N.A.'
//   }

const getCountriesPop = () => {
  let data = "data = [\n";
  for (const c of countriesPop) {
    data += `("${c["Country(ordependency)"]}", ${Number(
      c["Population(2023)"]
    )}),\n`;
  }
  data += "]";
  return data;
};

fs.writeFile(`../countries_pop.py`, getCountriesPop(), (err) => {
  if (err) throw err;
  console.log(`countries_pop.py written`);
});
