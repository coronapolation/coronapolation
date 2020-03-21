const Actions = {
    loadBundeslaender: (store) => {
        return API.bundeslaender(store.endpoint).then( data => {
            store.bundeslaender = data;
            store.notify();
        });
    }
};

const API = {
    fetch: (url, options, error) => {
        return fetch(url, options, error).catch(() => {
            return Promise.reject({error: "unable to reach " + url, status: null});
        }).then(response => {
            if (!response.ok) {
                return Promise.reject({error: error, status: response.status});
            }
            return response;
        });
    },
    fetchJSON: (url, options, error) => {
        return API.fetch(url, options, error).then(response => {
            return response.json();
        });
    },
    bundeslaender: (endpoint) => {
        return API.fetchJSON(endpoint + "/bundeslaender", {}, "unable to load bundeslaender").then(body => {
            return body;
        });
    }
};

export default Actions;
