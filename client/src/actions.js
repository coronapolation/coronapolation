const Actions = {
    loadBundeslaender: (store) => {
        return API.bundeslaender(store.endpoint).then( dictdata => {
            let data = [];
            for (var element in dictdata) {
                data.push({'id': element, 'name': dictdata[element]});
            }
            data.sort(function (a, b) {
                if(a.name < b.name) { return -1; }
                if(a.name > b.name) { return 1; }
                return 0;
            });
            store.bundeslaender = data;
            store.notify();
        });
    },
    loadLandkreise: (store, bundesland_id) => {
        return API.landkreise(store.endpoint, bundesland_id).then( dictdata => {
            let data = [];
            for (var element in dictdata) {
                data.push({'id': element, 'name': dictdata[element]});
            }
            data.sort(function (a, b) {
                if(a.name < b.name) { return -1; }
                if(a.name > b.name) { return 1; }
                return 0;
            });
            store.landkreise = data;
            store.notify();
        });
    },
    loadInfizierte: (store, landkreis_id) => {
        return API.infizierte(store.endpoint, landkreis_id).then( listdata => {
            let data = [];
            listdata.days.forEach(elem => {
                let listitem = {'name': elem[0]};
                listitem[landkreis_id] = elem[1];
                data.push(listitem)
            });
            store.infizierte = data;
            store.selected_landkreis_id = landkreis_id;
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
        return API.fetchJSON(endpoint + "/bundeslaender", {}, "unable to load bundeslaender").then( body => {
            return body;
        });
    },
    landkreise: (endpoint, bundesland_id) => {
        return API.fetchJSON(endpoint + "/landkreise/" + bundesland_id, {}, "unable to load landkreise").then( body => {
            return body;
        });
    },
    infizierte: (endpoint, landkreis_id) => {
        return API.fetchJSON(endpoint + "/infizierte/" + landkreis_id, {}, "unable to load infizierte").then( body => {
            return body;
        });
    }
};

export default Actions;
