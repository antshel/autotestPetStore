
class Endpoints:
    response = None
    response_json = None

    def status_code_is_200(self):
        assert self.response.status_code == 200

    def status_code_is_500(self):
        assert self.response.status_code == 500

    def status_code_is_404(self):
        assert self.response.status_code == 404

    def status_code_is_405(self):
        assert self.response.status_code == 405
     

    def status_code_is_400(self):
        assert self.response.status_code == 400

    def check_status_in_response(self, status):
        assert self.response_json['status'] == status
    
    def chek_name_pet_in_response(self, name):
        assert self.response_json['name'] == name

    def chek_id_pet_in_response(self, obj_id):
        assert self.response_json['id'] == obj_id