
const QuestionOptionComponent = (urlForm) => { 
    return {
        questions: [],

        init(){            
            this.questions = this.getJsonQuestions('#questions') || [];
            if (this.questions.length == 0)
               this.addEmptyQuestion();
        },

        getJsonQuestions(id){
            const elem = $(id);
            if(elem.length)
                return JSON.parse(elem.text());
            return null;
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
                $('textarea[name=questions_objects]').val(JSON.stringify(this.questions));
                $('#poll-form').submit();
            }
        },
        
    };
};
