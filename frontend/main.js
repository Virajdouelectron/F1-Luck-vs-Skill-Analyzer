// Loads CSVs and images from output/ and renders tables/plots
function loadCSVtoTable(csvPath, tableDivId) {
  fetch(csvPath)
    .then(resp => {
      if (!resp.ok) {
        console.error(`Failed to load ${csvPath}: ${resp.status} ${resp.statusText}`);
        return '';
      }
      return resp.text();
    })
    .then(text => {
      if (!text) return;
      const rows = text.trim().split('\n').map(r => r.split(','));
      if (rows.length < 2) {
        console.error(`No data in ${csvPath}`);
        return;
      }
      let html = '<table><thead><tr>' + rows[0].map(h => `<th>${h}</th>`).join('') + '</tr></thead><tbody>';
      for (let i = 1; i < Math.min(rows.length, 31); ++i) {
        html += '<tr>' + rows[i].map(d => `<td>${d}</td>`).join('') + '</tr>';
      }
      html += '</tbody></table>';
      document.getElementById(tableDivId).innerHTML = html;
    })
    .catch(error => {
      console.error(`Error loading ${csvPath}:`, error);
    });
}

// Function to load assumptions content
function loadAssumptions() {
  fetch('assumptions.html')
    .then(response => response.text())
    .then(html => {
      // Extract the content between <body> and </body> tags
      const bodyContent = html.match(/<body[^>]*>([\s\S]*)<\/body>/i)[1];
      document.getElementById('assumptions-content').innerHTML = bodyContent;
    })
    .catch(error => {
      console.error('Error loading assumptions:', error);
      document.getElementById('assumptions-content').innerHTML = 
        '<p>Failed to load assumptions. Please try refreshing the page.</p>';
    });
}

window.onload = function() {
  // Load tables with correct paths
  loadCSVtoTable('output/luck_adjusted_championship.csv', 'champ-table');
  loadCSVtoTable('output/luck_index_per_driver.csv', 'luck-table');
  loadCSVtoTable('output/most_lucky_per_season.csv', 'most-lucky');
  loadCSVtoTable('output/most_unlucky_per_season.csv', 'most-unlucky');
  
  // Load plots
  const plotYears = [];
  for (let year = 1950; year <= 1989; year++) {
    plotYears.push(year);
  }
  const html = plotYears.map(year => `<img src="output/luck_vs_skill_${year}.png" alt="Luck vs Skill ${year}">`).join('');
  document.getElementById('plots-gallery').innerHTML = html;
  
  // Load assumptions content
  loadAssumptions();
};
