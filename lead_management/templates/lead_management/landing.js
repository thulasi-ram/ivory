{% block content %}

$(document).ready(function() {
 var KanbanTest = new jKanban({
        element: '#kanban',
        gutter: '10px',
        dragBoards: false,
        widthBoard: '300px',
        click: function (el) {
            console.log("Trigger on all items click!");
        },
        dropEl: function (el, target, source, sibling) {
        alert("This will move " + el.textContent + ' from ' + $(source.parentElement).find('.kanban-title-board')[0].textContent + ' to ' + $(target.parentElement).find('.kanban-title-board')[0].textContent);
        $.ajax({
    url: '/lead_management/lead/' + el.textContent,
    type: 'PUT',
    data: {'stage': target.parentElement.getAttribute('data-id')},
    success: function(result) {
        console.log('Yay Success');
    }
});

        },
        dragEl: function (el, source) {
        window.KanbanItemBeingDragged = true;
        },
        dragendEl: function (el) {
        window.KanbanItemBeingDragged = false;

        },
        addItemButton: false,
        boards: [
            {
                "id": "_identify",
                "title": "Identify",
                "item": []
            },
            {
                "id": "_prospect",
                "title": "Prospects",
                "item": []
            },
            {
                "id": "_supporter",
                "title": "Supporters",
                "item": []
            },
            {
                "id": "_enquiry",
                "title": "Enquiry",
                "item": []
            },
            {
                "id": "_business",
                "title": "Business",
                "item": []
            }
        ]
    });


window.KanbanItemBeingDragged = false;
var myOffset = 0;
$('#slider_area').mousemove(function(event){
    if(window.KanbanItemBeingDragged == false) return;

    if ((event.pageX - this.offsetLeft) < $(this).width() / 2) {
        myOffset = myOffset - 100;

    } else {
        myOffset = myOffset + 100;
    }
     $('#kanban').animate({scrollLeft: myOffset}, 100);
});

function customize_board_css(self){
   self.find('.kanban-container').addClass('ui cards');
   self.find('.kanban-board').addClass('card');
   self.find('.kanban-item').addClass('ui segment');
}
customize_board_css($(this));
$("body").bind("DOMNodeInserted", function() {customize_board_css($(this))});


$('#add_lead').click(function(e) {
        window.open('{% url 'admin:lead_management_lead_add' %}', '_blank');
        <!--$('#add_contact_modal.ui.modal').modal('show');-->
    });

$.ajax({url: "{% url 'lead_management:leads' %}", success: function(leads){
        console.log(leads);
                leads.map(function( lead ) {
        KanbanTest.addElement('_'+ lead.stage, {
                    "title": lead.uid,
                })
        });
        }});
});

    function closed_leads_table() {
        if ($.fn.dataTable.isDataTable("#closed_leads_table")){
        return;
        }
        $('#closed_leads_table').DataTable({
            language: {
                search: "_INPUT_",
                searchPlaceholder: "Search..."
            },
            ajax: {
                url: "{% url 'lead_management:leads' %}" + '?stage=closed',
                dataSrc: ""
            },
            columns: [{
                    "data": "uid"
                },
                {
                    "data": "contact",
                    "render": function ( data, type, full, meta ) {
                                return '<a>' + data.client_account.name + '( ' + data.client_account.uid + ' )' + '</a>';}
                },
                {
                    "data": "contact",
                    "render": function ( data, type, full, meta ) {
                                return '<a>' + data.user.first_name + ' ' + data.user.last_name + '</a>';}
                }
            ]
        });
        $(".dataTables_filter label").addClass("ui input");

    }

    function tab_load(tab_name) {
        if (tab_name == 'closed_leads'){
        closed_leads_table()
        }
    }

    $('.menu .item').tab({'onFirstLoad':tab_load});

{% endblock %}