<template>
  <div id="app">
  <div class='container'>
    <div class='panel-group col-xs-6'>
        <div v-for="customer in customers" class='panel-primary'>
          <div class='panel-heading'>
            Name: {{ customer.name }}
          </div>
          <div class='panel-body'>
            <h6>
              Age: {{ customer.age }}
            </h6>
            <p>
              Balance: {{ customer.balance }}
            </p>
          </div>
        </div>
      </div>
    <div class='panel-group col-xs-6'>
        <div v-for="employee in employees" class='panel-primary'>
          <div class='panel-heading'>
            Name: {{ employee.name }}
          </div>
          <div class='panel-body'>
            <h6>
              Age: {{ employee.age }}
            </h6>
            <p>
              Title: {{ employee.title }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  created () {
    const customerXhr = new XMLHttpRequest();
    const customerRequest = new Promise((resolve, reject) => {
      customerXhr.open(`GET`, `/customers`);
      customerXhr.onload = (event) => {
        if (customerXhr.readyState === 4) {
          if (customerXhr.status === 200) {
            resolve(JSON.parse(customerXhr.response))
          } else {
            reject(customerXhr.statusText);
          }
        }
      };
      customerXhr.onerror = (event) => {
        reject(customerXhr.statusText);
      };
      customerXhr.setRequestHeader(`Content-Type`, `application/json;charset=UTF-8`);
      customerXhr.send(null);
    })
    .then((customers) => {
      this.customers = customers[0];
    })
    .catch((err) => {
      console.error(err);
    });
    const employeeXhr = new XMLHttpRequest();
    const employeeRequest = new Promise((resolve, reject) => {
      employeeXhr.open(`GET`, `/employees`);
      employeeXhr.onload = (event) => {
        if (employeeXhr.readyState === 4) {
          if (employeeXhr.status === 200) {
            resolve(JSON.parse(employeeXhr.response))
          } else {
            reject(employeeXhr.statusText);
          }
        }
      };
      employeeXhr.onerror = (event) => {
        reject(employeeXhr.statusText);
      };
      employeeXhr.setRequestHeader(`Content-Type`, `application/json;charset=UTF-8`);
      employeeXhr.send(null);
    })
    .then((employees) => {
      this.employees = employees[0];
    })
    .catch((err) => {
      console.error(err);
    });

  },
  data () {
    return {
      customers: [],
      employees: [],
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
