import { ApiService, IntegradorService } from './api.config'

export const GetUsers = () => {
  return new Promise(async resolve => {
    return ApiService.get('users')
      .then((response) => {
        resolve(response.data)
      })
      .catch(({ response }) => {
        resolve(response)
      })
  })
}

export const GetOneUser = (id) => {
  return new Promise(async resolve => {
    return ApiService.get('users/' + id)
      .then((response) => {
        resolve(response.data)
      })
      .catch(({ response }) => {
        resolve(response)
      })
  })
}

export const SaveUsers = (usuario) => {
  return new Promise(async resolve => {
    return ApiService.post('users', usuario)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}

export const UpdateUsers = (id, usuario) => {
  return new Promise(async resolve => {
    return ApiService.post('users/' + id, usuario)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}

export const changePass = (id, usuario) => {
  return new Promise(async resolve => {
    return ApiService.post('users/password/' + id, usuario)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}


export const DeleteUsers = (did) => {
  return new Promise(async resolve => {
    return ApiService.delete('users/' + did)
    .then(response => resolve(response))
    .catch(response => resolve(response));
  })
}

export const GetUnidadesSIPAF = () => {
  return new Promise(async resolve => {
    return IntegradorService.get()
      .then((response) => {
        resolve(response.data)
      })
      .catch(({ response }) => {
        resolve(response)
      })
  })
}