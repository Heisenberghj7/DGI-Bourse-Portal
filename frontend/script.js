const dataTable = document.getElementById('data-table');
const detailsSection = document.getElementById('details-section');
const detailsTable = document.getElementById('details-table');
const companyNameEl = document.getElementById('company-name');

let selectedCompany = "";

async function fetchData(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error("Failed to fetch data", error);
    }
}

async function displayData() {
    const keyFigureData = await fetchData('http://127.0.0.1:8000/api/keyfigure/');
    const publicationData = await fetchData('http://127.0.0.1:8000/api/publications/');

    keyFigureData
        .filter(kf => kf.year === "N-1")
        .forEach(kf => {
            const correspondingPublication = publicationData.find(pub => pub.company === kf.company);
            const newRow = dataTable.insertRow();
            
            const companyNameCell = newRow.insertCell();
            const companyLink = document.createElement('a');
            companyLink.href = "#";
            companyLink.innerText = kf.company;
            companyLink.onclick = (e) => {
                e.preventDefault();
                displayDetails(kf.company);
            };
            companyNameCell.appendChild(companyLink);
            
            newRow.insertCell().innerText = kf.sales_figures;
            newRow.insertCell().innerText = kf.net_income;
            newRow.insertCell().innerText = correspondingPublication?.title || '-';
            newRow.insertCell().innerText = correspondingPublication?.doc_info || '-';
        });
}

function displayDetails(company) {
  window.location.href = `details.html?company=${company}`;
}



async function fetchDetails(type) {
  if (type === 'contact') {
      // Handle contact display logic here
      // For now, we're simply clearing the table
      detailsTable.innerHTML = "";
      return;
  }
  
  const data = await fetchData(`http://127.0.0.1:8000/api/${type}/`);
  const relevantData = data.filter(item => item.company === selectedCompany);

  detailsTable.innerHTML = "";
  relevantData.forEach(item => {
      const newRow = detailsTable.insertRow();
      newRow.insertCell().innerText = item.name || item.holder;
      newRow.insertCell().innerText = item.post || item.percentage;
  });
}


displayData();
