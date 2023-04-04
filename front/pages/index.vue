<template>
  <v-app class="">
    <div class="grid grid-cols-12 mt-20">
      <div class="flex flex-col items-center col-span-6">
        <div class="font-bold text-9xl">
          Menu
        </div>
          <v-form class="flex flex-col mt-20" @submit.prevent = "send">
            <v-col>
              <v-text-field
                v-model="name"
                label="Nom"
                outlined
              ></v-text-field>

              <v-text-field
                v-model="couleur"
                label="Couleur"
                outlined
              ></v-text-field>

              <v-text-field
                v-model="prix"
                label="prix"
                outlined
              ></v-text-field>

              <v-btn outlined type="submit" @click="send" class="mt-3 ml-12">
                Button
              </v-btn>
            </v-col>
          </v-form>

      </div>

      <div class="col-span-6 mt-20 mr-20">
        <v-data-table
          :headers="header"
          :items="voitures"
          :items-per-page="10"
          class="elevation-1"
        ></v-data-table>
      </div>
    </div>

  </v-app>
</template>

<script>
export default {
  name: 'IndexPage',
  data(){
    return {
      voitures: null,
      name: null,
      couleur: null,
      prix: null
    }
  },
  methods: {
    send() {
      let data = {
        'name': this.name,
        'couleur': this.couleur,
        'prix': this.prix,
      }

      console.log(data)

      this.$axios.post('http://127.0.0.1:8000/testPost/', data)
    }
  },
  async asyncData({$axios}) {
    const response = await $axios.get('http://127.0.0.1:8000/')
    const voitures = response.data
    return {voitures}
  },
  computed: {
    header() {
      return [
        {text: 'Id', value: 'id_voiture'},
        { text: 'Nom', value: 'name' },
        { text: 'Couleur', value: 'couleur' },
        { text: 'Prix', value: 'prix' },
      ]
    }
  }
}
</script>

<style scoped lang="scss">



</style>
