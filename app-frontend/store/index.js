import axios from '~/plugins/myApiAxios'

export const state = () => ({
  garmentDisplayProperties: {},
  garmentDetails: {}
})

export const mutations = {
  UPDATE_GARMENT_DISPLAY_PROPERTIES(state, payload) {
    let properties = {
      count: payload.count,
      next: payload.next,
      previous: payload.previous
    }
    state.garmentDisplayProperties = properties
  },
  UPDATE_GARMENTS(state, payload) {
    state.garments = payload
  },
}
export const actions = {
  async fetchAllGarments({ commit }, pageParam = null) {
    let response
    if (pageParam === null) {
      // perform HTTP get without info for pagination (in case there's not that much data for Django backend to paginate or we want just the first page)
      response = await axios.get('garments/')
    } else {
      // else, if the page number is specified, ask our API for data for that page.
      response = await axios.get('garments/', {
        params: {
          page: pageParam
        }
      })
    }
    response = response.data
    commit('UPDATE_GARMENTS', response.results)
    commit('UPDATE_GARMENT_DISPLAY_PROPERTIES', response)
    return response
  },
  async searchGarment({ commit }, searchQuery) {
    let response = await axios.get('search/', {
      params: {
        q: searchQuery
      }
    })
    response = response.data
    commit('UPDATE_GARMENTS', response.results)
    commit('UPDATE_GARMENT_DISPLAY_PROPERTIES', response)
  },
  async searchPaginatedGarment({ commit }, payload) {
    let response = await axios.get('search/', {
      params: {
        page: payload.page,
        q: payload.q
      }
    })
    response = response.data
    commit('UPDATE_GARMENTS', response.results)
    commit('UPDATE_GARMENT_DISPLAY_PROPERTIES', response)
  },
}
