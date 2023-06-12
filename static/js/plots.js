//Grab data
let industry_data = "/api/v1.0/quitrates_covid19_byindustry";

d3.json(industry_data).then(function(data){
    // data is an array that is 5 members long
    for (let i=0; i<data.length; i++) {
        let entry = data[i];
        let title = data.Industry;
        let xArray = [2018,2019,2020,2021,2022];
        let yArray = [data["2018"],
        data["2019"],
        data["2020"],
        data["2021"],
        data["2022"]];        
    }
});

// function init() {
//   // let dropdown = d3.select("#selDataset")
//   d3.json(industry_data).then(function (data) {
//       let industry = data.Industry
//       for (let i = 0; i < industry.length; i++) {
//           dropdown.append("option").text(industry[i]).property("value", industry[i])
//       }
//       // console.log(data);
//       let firstindustry = industry[0]
//       showbubblechart(firstindustry)
//   });
// };

// init();

// function optionChanged(newindustry) {
//   showbubblechart(newindustry)
// }

function showbubblechart(industry) {
  d3.json(industry_data).then(function (data) {
      let industry = data.Industry
      let industryarray = industry.filter(firstindustry => firstindustry == industry)
      let firstindustry = industryarray[0]
      let rate_2018 = firstindustry.column_2018
      let rate_2019 = firstindustry.column_2019
      let rate_2020 = firstindustry.column_2020
      let rate_2021 = firstindustry.column_2021
      let rate_2022 = firstindustry.column_2022

      console.log(rate_2018)

let trace1 = {
  x: xArray,
  y: yArray,
  text: industry,
  mode: "markers",
marker: {
  color: industry,
  size: yArray
}
};
  
let dataPlot1 = [trace1];

// Apply a title to the layout
let layout = {
  showlegend: false,
height: 500,
width: 900
}

Plotly.newPlot("bubble", dataPlot1, layout);
});

};

// // Create an array of each country's numbers
// let Construction = Object.values(data.Construction);
// let RetailTrade = Object.values(data.RetailTrade);
// let Transportation_Warehousing_Utilities= Object.values(data.Transportation_Warehousing_Utilities);
// let Arts_Entertainment_Recreation= Object.values(data.Arts_Entertainment_Recreation);
// let Accommodation_FoodServices= Object.values(data.Accommodation_FoodServices);

// // Create an array of category labels
// let labels = Object.keys(data.Construction);
// // console.log(Construction);

// function updatePlot() {
//     let dropdownMenu = d3.select("#selDataset");
//     let datasetName = dropdownMenu.property("value");

//     let x = [];
//     let y = labels;

//     if (datasetName == 'Construction') {
//     x = Construction;
//     }
//     else if (datasetName == 'RetailTrade') {
//       x = RetailTrade;
//     }
//     else if (datasetName == 'Transportation_Warehousing_Utilities') {
//       x = Transportation_Warehousing_Utilities;
//      }
//      else if (datasetName == 'Arts_Entertainment_Recreation') {
//     x = Arts_Entertainment_Recreation;
//      }
//     else if (datasetName == 'Accommodation_FoodServices') {
//       x = Accommodation_FoodServices;
//     }

//     Plotly.restyle("bubble", "values", [x]);
// }

// let myDropDown = d3.select("#selDataset")
// myDropDown.on("click", updatePlot);

// init();

// console.log(x)



// // On change to the DOM, call getData()
// d3.selectAll("#selDataset").on("change", getData);

// // Function called by DOM changes
// function getData() {
//   let dropdownMenu = d3.select("#selDataset");
//   // Assign the value of the dropdown menu option to a letiable
//   let dataset = dropdownMenu.property("value");
//   // Initialize an empty array for the country's data
//   let data = [];

//   if (dataset == 'Construction') {
//       data = Construction;
//   }
//   else if (dataset == 'RetailTrade') {
//       data = RetailTrade;
//   }
//   else if (dataset == 'Transportation, Warehousing, Utilities') {
//       data = Transportation, Warehousing, Utilities;
//   }
//   else if (dataset == 'Arts, Entertainment, Recreation') {
//     data = Arts, Entertainment, Recreation;
//   }
//   else if (dataset == 'Accommodation, FoodServices') {
//       data = Accommodation, FoodServices;
//   }
// // Call function to update the chart
//   updatePlotly(data);
// }

// // Update the restyled plot's values
// function updatePlotly(newdata) {
//   Plotly.restyle("bubble", "values", [newdata]);
// }

// init();


