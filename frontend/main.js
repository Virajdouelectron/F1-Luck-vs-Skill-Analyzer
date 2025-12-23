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
      document.getElementById(tableDivId).innerHTML = html;
    });
}
window.onload = function() {
  loadCSVtoTable('../output/luck_adjusted_championship.csv', 'champ-table');
  loadCSVtoTable('../output/luck_index_per_driver.csv', 'luck-table');
  loadCSVtoTable('../output/most_lucky_per_season.csv', 'most-lucky');
  loadCSVtoTable('../output/most_unlucky_per_season.csv', 'most-unlucky');
  // Load plots
  fetch('../output/')
    .then(resp => resp.text())
    .then(text => {
      const plotImgs = [];
      const re = /luck_vs_skill_(\d+)\.png/g;
      let m;
      while ((m = re.exec(text)) !== null) {
        plotImgs.push(m[0]);
      }
      let html = plotImgs.map(f => `<img src="../output/${f}" alt="Luck vs Skill ${f.replace(/[^\d]/g,'')}">`).join('');
      document.getElementById('plots-gallery').innerHTML = html;
    });
};
