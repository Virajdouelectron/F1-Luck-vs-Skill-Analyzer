// Loads CSVs and images from output/ and renders tables/plots
function loadCSVtoTable(csvPath, tableDivId) {
  fetch(csvPath)
    .then(resp => resp.text())
    .then(text => {
      const rows = text.trim().split('\n').map(r => r.split(','));
      let html = '<table><thead><tr>' + rows[0].map(h => `<th>${h}</th>`).join('') + '</tr></thead><tbody>';
      for (let i = 1; i < Math.min(rows.length, 31); ++i) {
        html += '<tr>' + rows[i].map(d => `<td>${d}</td>`).join('') + '</tr>';
      }
      html += '</tbody></table>';
    });
}
window.onload = function() {
  loadCSVtoTable('../output/luck_adjusted_championship.csv', 'champ-table');
  loadCSVtoTable('../output/luck_index_per_driver.csv', 'luck-table');
  // List all PNGs found in output/ (years 1950-1989 as detected)
  const plotYears = [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989];
  let html = plotYears.map(year => `<img src="output/luck_vs_skill_${year}.png" alt="Luck vs Skill ${year}">`).join('');
  document.getElementById('plots-gallery').innerHTML = html;
};
