const express = require('express')
const mongoose = require('mongoose')
const exphbs = require('express-handlebars')
const todosRoutes = require('./routes/todos')



const PORT =  process.env.PORT || 3000

const app = express()
const hbs = exphbs.create({
    defaultLayout: 'main',
    extname: 'hbs'
})

app.engine('hbs', hbs.engine)
app.set('view engine', 'hbs')
app.set('views', 'views')

app.use(express.urlencoded({extended: true}))
app.use(todosRoutes)



async function start(){
    try {
        await mongoose.connect(
            'mongodb+srv://andrei:andrei@cluster0.0hipu.mongodb.net/todos',
            {
            useNewUrlParser: true,
            useFindAndModify: false
        })
        app.listen(PORT, () => {
            console.log('Server started...')
        })        
    } catch (e) {
        console.log(e)
    }

}



start()





