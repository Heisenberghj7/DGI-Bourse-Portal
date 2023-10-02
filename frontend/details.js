const detailsTable = document.getElementById('details-table');
const companyNameEl = document.getElementById('company-name');

let selectedCompany = new URLSearchParams(window.location.search).get('company');

async function fetchData(url) {
    try {
        const response = await fetch(url);
        return await response.json();
    } catch (error) {
        console.error("Failed to fetch data", error);
    }
}

function displayDetails() {
    companyNameEl.innerText = selectedCompany;
}


async function fetchDetails(type) {
  // Clear existing table data and headers
  detailsTable.innerHTML = "";

  // Set table headers based on the type
  const headerRow = detailsTable.insertRow();
  if (type === 'shareholder') {
      headerRow.insertCell().innerText = "Holder";
      headerRow.insertCell().innerText = "Percentage";
  } else if (type === 'contact') {
      headerRow.insertCell().innerText = "Name";
      headerRow.insertCell().innerText = "Email";
      headerRow.insertCell().innerText = "Phone";
      headerRow.insertCell().innerText = "Fax";
      headerRow.insertCell().innerText = "Website";
  } else if (type === 'management') {
      headerRow.insertCell().innerText = "Name";
      headerRow.insertCell().innerText = "Post";
  } 

  const data = await fetchData(`http://127.0.0.1:8000/api/${type}/`);
  const relevantData = data.find(item => item.name === selectedCompany);

  if (type === 'companies' && relevantData) {
      for (const key in relevantData) {
          if (key !== 'name') {
              const newRow = detailsTable.insertRow();
              newRow.insertCell().innerText = key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, ' '); // Convert attribute names into a readable format
              newRow.insertCell().innerText = relevantData[key];
          }
      }
  } else {
      const items = data.filter(item => item.company === selectedCompany);
      items.forEach(item => {
          const newRow = detailsTable.insertRow();
          if (type === 'shareholder') {
              newRow.insertCell().innerText = item.holder;
              newRow.insertCell().innerText = item.percentage;
          } else if (type === 'contact') {
              newRow.insertCell().innerText = item.name;
              newRow.insertCell().innerText = item.mail;
              newRow.insertCell().innerText = item.phone;
              newRow.insertCell().innerText = item.fax;
              newRow.insertCell().innerText = item.website;
          } else if (type === 'management') {
              newRow.insertCell().innerText = item.name;
              newRow.insertCell().innerText = item.post;
          }
      });
  }
}





displayDetails();
