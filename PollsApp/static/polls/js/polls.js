const QuestionOptionComponent = {
    questions: [],

    init(){
        this.addEmptyQuestion(); 
    },

    addEmptyQuestion(){
        this.questions.push({
            id:null,
            sentence:'',
            type_question:'',
            options:[
                {
                    id:null,
                    sentence:''
                }
            ],
        });
    },

    addEmptyOption(index){
        this.questions[index].options.push({
            id:null,
            sentence:''
        });
    },

    removeQuestion(indexQuestion){
        this.questions = this.questions.filter((_, i) => i !== indexQuestion);
    },

    removeOption(indexQuestion, indexOption){
        this.questions[indexQuestion].options = this.questions[indexQuestion]
            .options.filter((_, i) => i !== indexOption);
    },

    
    buttonAction:{
        ['@click'](){
            console.log(this.questions);
            console.log(JSON.parse(JSON.stringify(this.questions)));

            $('textarea[name=questions_objects]').val(JSON.stringify(this.questions));
            $('#poll-form').submit()
        }
    },
    
};