<template>
  <div v-if="!loading" class="">
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
              ></v-text-field>

              <v-text-field
                v-model="couleur"
                label="Couleur"
              ></v-text-field>

              <v-text-field
                v-model="prix"
                label="prix"
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
        >
          <template v-slot:item.actions="{ item }">
            <v-icon class="hover:bg-gray-300 cursor-pointer rounded-full" @click="deleteVoiture(item)">
              mdi-delete
            </v-icon>

            <v-icon class="hover:bg-gray-300 cursor-pointer rounded-full" @click="updateVoiture(item)">
              mdi-pencil
            </v-icon>
          </template>

        </v-data-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data(){
    return {
      voitures: null,
      name: null,
      couleur: null,
      prix: null,
      loading:false,
      initialData: null,
      pageList: ['Page1', 'Page2', 'Page3', 'Page4', 'Page5', 'Page6']
    }
  },
  methods: {
    send() {
      this.loading = true

      let data = {
        'name': this.name,
        'couleur': this.couleur,
        'prix': parseInt(this.prix),
      }

      this.$axios.post('http://127.0.0.1:8000/testBack/voiture/', data).then(() => {

        this.voitures.push({
            name: this.name,
            couleur: this.couleur,
            prix: parseInt(this.prix)
        })
        this.name = ''
        this.couleur = ''
        this.prix = ''

      }).finally(() => {
        this.$nextTick(() => {
          this.loading = false
        })
      })
    },
    updateVoiture(voiture) {
      this.loading = true

      if (voiture.name === "UPDATE") {
        voiture.name = "NOT"
      } else {
        voiture.name = "UPDATE"
      }

      let data = {...voiture}

      this.$axios.put('http://127.0.0.1:8000/testBack/voiture/', data).then(() => {
        this.$set(this.voitures, this.voitures.indexOf(voiture), voiture)
        this.loading = false
      })

    },
    deleteVoiture(voiture) {
      let config = {
        data: {
          id: this.voitures[this.voitures.indexOf(voiture)].id_voiture
        }
      }
      this.$axios.delete('http://127.0.0.1:8000/testBack/voiture/', config).then(() => {
      }).finally(() => {
        this.$nextTick(() => {
          this.loading = false
        })
      })

      this.voitures.splice(this.voitures.indexOf(voiture), 1)
    }
  },
  async asyncData({$axios}) {
    const response = await $axios.get('http://127.0.0.1:8000/testBack/voiture/')
    const voitures = response.data
    const initialData = response.data
    return {voitures, initialData}
  },
  computed: {
    header() {
      return [
        { text: 'Nom', value: 'name' },
        { text: 'Couleur', value: 'couleur' },
        { text: 'Prix', value: 'prix' },
        {text: 'Action', value:'actions'}
      ]
    }
  },
  updated() {
    console.log("la")
  }
}
</script>

<style scoped lang="scss">



</style>
