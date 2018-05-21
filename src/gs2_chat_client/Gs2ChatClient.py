# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2ChatClient(AbstractGs2Client):

    ENDPOINT = "chat"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2ChatClient, self).__init__(credential, region)

    def create_lobby(self, request):
        """
        ロビーを新規作成します<br>
        <br>
        GS2-Chat の使用を開始するには、まずはロビーを作成します。<br>
        ロビーはチャットルームの集合体のような存在です。<br>
        <br>
        ロビーへの設定項目として購読しているルームに発言があったときの通知方式を指定できます。<br>
        http/https を設定した場合は、新しい発言があるたびに指定されたURLに通知を出します。<br>
        通知は以下のフォーマットで通知されます。<br>
        {<br>
          "_gs2_service": "GS2-Chat#Receive",<br>
          "notificationUserIds": [<br>
            通知先ユーザID<br>
          ],<br>
          "roomId": 発言されたルームID,<br>
          "userId": 発言したユーザのユーザID,<br>
          "message": {<br>
            "text": メッセージテキスト,<br>
            "meta": メタデータ,<br>
          }<br>
        }<br>
        GS2-InGamePushNotification を指定した場合は、新しい発言があるたびにプッシュ通知を出します。<br>
        通知は以下のフォーマットで通知されます。<br>
        {<br>
          "subject": メッセージテキスト,<br>
          "body": {<br>
            "_gs2_service": "GS2-Chat#Receive",<br>
            "roomId": 発言されたルームID,<br>
            "userId": 発言したユーザのユーザID,<br>
            "message": {<br>
              "text": メッセージテキスト,<br>
              "meta": メタデータ,<br>
            }<br>
          }<br>
        }<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CreateLobbyRequest.CreateLobbyRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CreateLobbyResult.CreateLobbyResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
            "notificationType": request.get_notification_type(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        if request.get_logging() is not None:
            body["logging"] = request.get_logging()
        if request.get_logging_date() is not None:
            body["loggingDate"] = request.get_logging_date()
        if request.get_create_room_trigger_script() is not None:
            body["createRoomTriggerScript"] = request.get_create_room_trigger_script()
        if request.get_create_room_done_trigger_script() is not None:
            body["createRoomDoneTriggerScript"] = request.get_create_room_done_trigger_script()
        if request.get_delete_room_trigger_script() is not None:
            body["deleteRoomTriggerScript"] = request.get_delete_room_trigger_script()
        if request.get_delete_room_done_trigger_script() is not None:
            body["deleteRoomDoneTriggerScript"] = request.get_delete_room_done_trigger_script()
        if request.get_create_subscribe_trigger_script() is not None:
            body["createSubscribeTriggerScript"] = request.get_create_subscribe_trigger_script()
        if request.get_create_subscribe_done_trigger_script() is not None:
            body["createSubscribeDoneTriggerScript"] = request.get_create_subscribe_done_trigger_script()
        if request.get_delete_subscribe_trigger_script() is not None:
            body["deleteSubscribeTriggerScript"] = request.get_delete_subscribe_trigger_script()
        if request.get_delete_subscribe_done_trigger_script() is not None:
            body["deleteSubscribeDoneTriggerScript"] = request.get_delete_subscribe_done_trigger_script()
        if request.get_send_message_trigger_script() is not None:
            body["sendMessageTriggerScript"] = request.get_send_message_trigger_script()
        if request.get_send_message_done_trigger_script() is not None:
            body["sendMessageDoneTriggerScript"] = request.get_send_message_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CreateLobbyRequest import CreateLobbyRequest
        from gs2_chat_client.control.CreateLobbyResult import CreateLobbyResult
        return CreateLobbyResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby",
            service=self.ENDPOINT,
            component=CreateLobbyRequest.Constant.MODULE,
            target_function=CreateLobbyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_lobby(self, request):
        """
        ロビーを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DeleteLobbyRequest.DeleteLobbyRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DeleteLobbyRequest import DeleteLobbyRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteLobbyRequest.Constant.MODULE,
            target_function=DeleteLobbyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_lobby(self, request):
        """
        ロビーの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeLobbyRequest.DescribeLobbyRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeLobbyResult.DescribeLobbyResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeLobbyRequest import DescribeLobbyRequest

        from gs2_chat_client.control.DescribeLobbyResult import DescribeLobbyResult
        return DescribeLobbyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby",
            service=self.ENDPOINT,
            component=DescribeLobbyRequest.Constant.MODULE,
            target_function=DescribeLobbyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_chat_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/serviceClass",
            service=self.ENDPOINT,
            component=DescribeServiceClassRequest.Constant.MODULE,
            target_function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_lobby(self, request):
        """
        ロビーを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.GetLobbyRequest.GetLobbyRequest
        :return: 結果
        :rtype: gs2_chat_client.control.GetLobbyResult.GetLobbyResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.GetLobbyRequest import GetLobbyRequest

        from gs2_chat_client.control.GetLobbyResult import GetLobbyResult
        return GetLobbyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "",
            service=self.ENDPOINT,
            component=GetLobbyRequest.Constant.MODULE,
            target_function=GetLobbyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_lobby_status(self, request):
        """
        ロビーの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.GetLobbyStatusRequest.GetLobbyStatusRequest
        :return: 結果
        :rtype: gs2_chat_client.control.GetLobbyStatusResult.GetLobbyStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.GetLobbyStatusRequest import GetLobbyStatusRequest

        from gs2_chat_client.control.GetLobbyStatusResult import GetLobbyStatusResult
        return GetLobbyStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/status",
            service=self.ENDPOINT,
            component=GetLobbyStatusRequest.Constant.MODULE,
            target_function=GetLobbyStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_lobby(self, request):
        """
        ロビーを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.UpdateLobbyRequest.UpdateLobbyRequest
        :return: 結果
        :rtype: gs2_chat_client.control.UpdateLobbyResult.UpdateLobbyResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
            "notificationType": request.get_notification_type(),
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_notification_game_name() is not None:
            body["notificationGameName"] = request.get_notification_game_name()
        if request.get_logging() is not None:
            body["logging"] = request.get_logging()
        if request.get_logging_date() is not None:
            body["loggingDate"] = request.get_logging_date()
        if request.get_create_room_trigger_script() is not None:
            body["createRoomTriggerScript"] = request.get_create_room_trigger_script()
        if request.get_create_room_done_trigger_script() is not None:
            body["createRoomDoneTriggerScript"] = request.get_create_room_done_trigger_script()
        if request.get_delete_room_trigger_script() is not None:
            body["deleteRoomTriggerScript"] = request.get_delete_room_trigger_script()
        if request.get_delete_room_done_trigger_script() is not None:
            body["deleteRoomDoneTriggerScript"] = request.get_delete_room_done_trigger_script()
        if request.get_create_subscribe_trigger_script() is not None:
            body["createSubscribeTriggerScript"] = request.get_create_subscribe_trigger_script()
        if request.get_create_subscribe_done_trigger_script() is not None:
            body["createSubscribeDoneTriggerScript"] = request.get_create_subscribe_done_trigger_script()
        if request.get_delete_subscribe_trigger_script() is not None:
            body["deleteSubscribeTriggerScript"] = request.get_delete_subscribe_trigger_script()
        if request.get_delete_subscribe_done_trigger_script() is not None:
            body["deleteSubscribeDoneTriggerScript"] = request.get_delete_subscribe_done_trigger_script()
        if request.get_send_message_trigger_script() is not None:
            body["sendMessageTriggerScript"] = request.get_send_message_trigger_script()
        if request.get_send_message_done_trigger_script() is not None:
            body["sendMessageDoneTriggerScript"] = request.get_send_message_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.UpdateLobbyRequest import UpdateLobbyRequest
        from gs2_chat_client.control.UpdateLobbyResult import UpdateLobbyResult
        return UpdateLobbyResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateLobbyRequest.Constant.MODULE,
            target_function=UpdateLobbyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def check_estimate_scan_byte_by_all_room(self, request):
        """
        メッセージ検索時にスキャンするログサイズの予測値を取得します。<br>
        <br>
        長期にわたる検索を行う場合、事前におおよそのログスキャン容量を把握したいと思うはずです。<br>
        そのような場合にはこのAPIを使用することで、事前にログスキャン容量を把握することが出来ます。<br>
        <br>
        ただし、ここで得られる値はあくまで予測値であり、実際に実行した際の値とは異なる場合があります。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CheckEstimateScanByteByAllRoomRequest.CheckEstimateScanByteByAllRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CheckEstimateScanByteByAllRoomResult.CheckEstimateScanByteByAllRoomResult
        """
        query_strings = {
            'userId': request.get_user_id(),
            'message': request.get_message(),
            'meta': request.get_meta(),
            'begin': request.get_begin(),
            'end': request.get_end(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CheckEstimateScanByteByAllRoomRequest import CheckEstimateScanByteByAllRoomRequest

        from gs2_chat_client.control.CheckEstimateScanByteByAllRoomResult import CheckEstimateScanByteByAllRoomResult
        return CheckEstimateScanByteByAllRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/log/estimate",
            service=self.ENDPOINT,
            component=CheckEstimateScanByteByAllRoomRequest.Constant.MODULE,
            target_function=CheckEstimateScanByteByAllRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def check_estimate_scan_byte_by_room(self, request):
        """
        メッセージ検索時にスキャンするログサイズの予測値を取得します。<br>
        <br>
        長期にわたる検索を行う場合、事前におおよそのログスキャン容量を把握したいと思うはずです。<br>
        そのような場合にはこのAPIを使用することで、事前にログスキャン容量を把握することが出来ます。<br>
        <br>
        ただし、ここで得られる値はあくまで予測値であり、実際に実行した際の値とは異なる場合があります。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CheckEstimateScanByteByRoomRequest.CheckEstimateScanByteByRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CheckEstimateScanByteByRoomResult.CheckEstimateScanByteByRoomResult
        """
        query_strings = {
            'userId': request.get_user_id(),
            'message': request.get_message(),
            'meta': request.get_meta(),
            'begin': request.get_begin(),
            'end': request.get_end(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CheckEstimateScanByteByRoomRequest import CheckEstimateScanByteByRoomRequest

        from gs2_chat_client.control.CheckEstimateScanByteByRoomResult import CheckEstimateScanByteByRoomResult
        return CheckEstimateScanByteByRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/log/estimate",
            service=self.ENDPOINT,
            component=CheckEstimateScanByteByRoomRequest.Constant.MODULE,
            target_function=CheckEstimateScanByteByRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def search_log_by_all_room(self, request):
        """
        メッセージログを検索します。<br>
        <br>
        メッセージログの検索には以下のパラメータを使用できます。<br>
        * ユーザID<br>
        * メッセージテキスト<br>
        * メッセージメタデータ<br>
        いずれも部分一致で検索できます。<br>
        たとえば、メッセージメタデータに JSON フォーマットを使用している場合は JSON 文字列に対する部分一致検索が適用できます。<br>
        一方で、BLOB データを Base64 かけたようなデータの場合は検索対象とするのは困難です。<br>
        <br>
        メッセージログ検索にかかる費用は、検索時にログデータを何バイトスキャンしたかで決定されます。<br>
        そのため、発言者が滞在していたルームが特定できている場合は、本APIではなく『Gs2Chat:SearchLogByRoom』を使用する方が費用を節約できます。<br>
        また、検索範囲を時間で指定できますが、ログデータは1日単位(UTC)で分割して保存されており、スキャン時には1日分全てがスキャン対象となります。<br>
        つまり、特定の日付の5分間のログを検索するクエリを実行した場合、該当する1日分のログデータがスキャン対象となり、<br>
        さらにその5分間が日付をまたぐような場合は2日分のログデータがスキャン対象となります。<br>
        <br>
        検索結果が指定した取得最大件数以上の結果を持つ場合、実行後一定期間内であればページトークンを使用した続きのデータ取得が可能です。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.SearchLogByAllRoomRequest.SearchLogByAllRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.SearchLogByAllRoomResult.SearchLogByAllRoomResult
        """
        query_strings = {
            'userId': request.get_user_id(),
            'message': request.get_message(),
            'meta': request.get_meta(),
            'begin': request.get_begin(),
            'end': request.get_end(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
            'useCache': request.get_use_cache(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.SearchLogByAllRoomRequest import SearchLogByAllRoomRequest

        from gs2_chat_client.control.SearchLogByAllRoomResult import SearchLogByAllRoomResult
        return SearchLogByAllRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/log",
            service=self.ENDPOINT,
            component=SearchLogByAllRoomRequest.Constant.MODULE,
            target_function=SearchLogByAllRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def search_log_by_room(self, request):
        """
        メッセージログを検索します。<br>
        <br>
        メッセージログの検索には以下のパラメータを使用できます。<br>
        * ユーザID<br>
        * メッセージテキスト<br>
        * メッセージメタデータ<br>
        いずれも部分一致で検索できます。<br>
        たとえば、メッセージメタデータに JSON フォーマットを使用している場合は JSON 文字列に対する部分一致検索が適用できます。<br>
        一方で、BLOB データを Base64 かけたようなデータの場合は検索対象とするのは困難です。<br>
        <br>
        メッセージログ検索にかかる費用は、検索時にログデータを何バイトスキャンしたかで決定されます。<br>
        検索範囲を時間で指定できますが、ログデータは1日単位(UTC)で分割して保存されており、スキャン時には1日分全てがスキャン対象となります。<br>
        つまり、特定の日付の5分間のログを検索するクエリを実行した場合、該当する1日分のログデータがスキャン対象となり、<br>
        さらにその5分間が日付をまたぐような場合は2日分のログデータがスキャン対象となります。<br>
        <br>
        検索結果が指定した取得最大件数以上の結果を持つ場合、実行後一定期間内であればページトークンを使用した続きのデータ取得が可能です。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.SearchLogByRoomRequest.SearchLogByRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.SearchLogByRoomResult.SearchLogByRoomResult
        """
        query_strings = {
            'userId': request.get_user_id(),
            'message': request.get_message(),
            'meta': request.get_meta(),
            'begin': request.get_begin(),
            'end': request.get_end(),
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
            'useCache': request.get_use_cache(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.SearchLogByRoomRequest import SearchLogByRoomRequest

        from gs2_chat_client.control.SearchLogByRoomResult import SearchLogByRoomResult
        return SearchLogByRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/log",
            service=self.ENDPOINT,
            component=SearchLogByRoomRequest.Constant.MODULE,
            target_function=SearchLogByRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_message(self, request):
        """
        メッセージの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeMessageRequest.DescribeMessageRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeMessageResult.DescribeMessageResult
        """
        query_strings = {
            'password': request.get_password(),
            'startAt': request.get_start_at(),
            'limit': request.get_limit(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeMessageRequest import DescribeMessageRequest

        from gs2_chat_client.control.DescribeMessageResult import DescribeMessageResult
        return DescribeMessageResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/message",
            service=self.ENDPOINT,
            component=DescribeMessageRequest.Constant.MODULE,
            target_function=DescribeMessageRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_message_no_auth(self, request):
        """
        メッセージの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeMessageNoAuthRequest.DescribeMessageNoAuthRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeMessageNoAuthResult.DescribeMessageNoAuthResult
        """
        query_strings = {
            'startAt': request.get_start_at(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeMessageNoAuthRequest import DescribeMessageNoAuthRequest

        from gs2_chat_client.control.DescribeMessageNoAuthResult import DescribeMessageNoAuthResult
        return DescribeMessageNoAuthResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/message/force",
            service=self.ENDPOINT,
            component=DescribeMessageNoAuthRequest.Constant.MODULE,
            target_function=DescribeMessageNoAuthRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def send_message(self, request):
        """
        メッセージを送信します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.SendMessageRequest.SendMessageRequest
        :return: 結果
        :rtype: gs2_chat_client.control.SendMessageResult.SendMessageResult
        """
        body = { 
            "message": request.get_message(),
        }

        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_password() is not None:
            body["password"] = request.get_password()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.SendMessageRequest import SendMessageRequest
        from gs2_chat_client.control.SendMessageResult import SendMessageResult
        return SendMessageResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/message",
            service=self.ENDPOINT,
            component=SendMessageRequest.Constant.MODULE,
            target_function=SendMessageRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def send_message_no_auth(self, request):
        """
        メッセージを送信します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.SendMessageNoAuthRequest.SendMessageNoAuthRequest
        :return: 結果
        :rtype: gs2_chat_client.control.SendMessageNoAuthResult.SendMessageNoAuthResult
        """
        body = { 
            "userId": request.get_user_id(),
            "message": request.get_message(),
        }

        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.SendMessageNoAuthRequest import SendMessageNoAuthRequest
        from gs2_chat_client.control.SendMessageNoAuthResult import SendMessageNoAuthResult
        return SendMessageNoAuthResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/message/force",
            service=self.ENDPOINT,
            component=SendMessageNoAuthRequest.Constant.MODULE,
            target_function=SendMessageNoAuthRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_room(self, request):
        """
        ルームを作成します<br>
        <br>
        ルームには参加可能なユーザIDリストを設定することが出来ます。<br>
        ここで指定されたユーザID以外のユーザがメッセージ情報を取得したり、メッセージを書き込もうとしても失敗するようになります。<br>
        何も指定しなければ、誰でも読み書きの出来る部屋になります。<br>
        ルームを作成する際に参加するユーザが確定している場合に使用するといいでしょう。<br>
        <br>
        ルームにはパスワードを設定することが出来ます。<br>
        パスワードが設定されたルームのメッセージ情報を取得したり、メッセージを書き込もうとするさいにパスワードを指定する必要があります。<br>
        パスワードが一致しない場合は失敗します。<br>
        何も指定しなければ、メッセージの読み書きにパスワードを要求しません。<br>
        ルームを作成する際には参加するユーザが確定できないけれど、アクセスを制限したい場合に使用するといいでしょう。<br>
        <br>
        ルームIDには任意の値を指定することが出来ます。<br>
        たとえば、マッチメイキングを実行し構築されたギャザリングのユーザ向けにチャットルームを提供したい場合、<br>
        ギャザリングIDをキーとしてルームを作成することで、クライアントがチャットにアクセスする際にIDの特定が容易になります。<br>
        ルームIDを省略するとUUIDv4に基づいて自動的に採番されます。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CreateRoomRequest.CreateRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CreateRoomResult.CreateRoomResult
        """
        body = { 
        }

        if request.get_room_id() is not None:
            body["roomId"] = request.get_room_id()
        if request.get_allow_user_ids() is not None:
            body["allowUserIds"] = request.get_allow_user_ids()
        if request.get_password() is not None:
            body["password"] = request.get_password()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CreateRoomRequest import CreateRoomRequest
        from gs2_chat_client.control.CreateRoomResult import CreateRoomResult
        return CreateRoomResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room",
            service=self.ENDPOINT,
            component=CreateRoomRequest.Constant.MODULE,
            target_function=CreateRoomRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_room(self, request):
        """
        ルームを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DeleteRoomRequest.DeleteRoomRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DeleteRoomRequest import DeleteRoomRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "",
            service=self.ENDPOINT,
            component=DeleteRoomRequest.Constant.MODULE,
            target_function=DeleteRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_room(self, request):
        """
        ルームの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeRoomRequest.DescribeRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeRoomResult.DescribeRoomResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeRoomRequest import DescribeRoomRequest

        from gs2_chat_client.control.DescribeRoomResult import DescribeRoomResult
        return DescribeRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room",
            service=self.ENDPOINT,
            component=DescribeRoomRequest.Constant.MODULE,
            target_function=DescribeRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_room(self, request):
        """
        ルームを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.GetRoomRequest.GetRoomRequest
        :return: 結果
        :rtype: gs2_chat_client.control.GetRoomResult.GetRoomResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.GetRoomRequest import GetRoomRequest

        from gs2_chat_client.control.GetRoomResult import GetRoomResult
        return GetRoomResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "",
            service=self.ENDPOINT,
            component=GetRoomRequest.Constant.MODULE,
            target_function=GetRoomRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_my_subscribe(self, request):
        """
        ルームを購読します。<br>
        <br>
        ルームを購読すると、ルームに対する新着メッセージを受信したときに通知を受けることが出来ます。<br>
        通知方式はロビーの設定に依存します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CreateMySubscribeRequest.CreateMySubscribeRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CreateMySubscribeResult.CreateMySubscribeResult
        """
        body = { 
        }

        if request.get_enable_offline_transfer() is not None:
            body["enableOfflineTransfer"] = request.get_enable_offline_transfer()
        if request.get_offline_transfer_sound() is not None:
            body["offlineTransferSound"] = request.get_offline_transfer_sound()
        if request.get_password() is not None:
            body["password"] = request.get_password()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CreateMySubscribeRequest import CreateMySubscribeRequest
        from gs2_chat_client.control.CreateMySubscribeResult import CreateMySubscribeResult
        return CreateMySubscribeResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=CreateMySubscribeRequest.Constant.MODULE,
            target_function=CreateMySubscribeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_subscribe(self, request):
        """
        ルームを購読します。<br>
        <br>
        ルームを購読すると、ルームに対する新着メッセージを受信したときに通知を受けることが出来ます。<br>
        通知方式はロビーの設定に依存します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.CreateSubscribeRequest.CreateSubscribeRequest
        :return: 結果
        :rtype: gs2_chat_client.control.CreateSubscribeResult.CreateSubscribeResult
        """
        body = { 
        }

        if request.get_enable_offline_transfer() is not None:
            body["enableOfflineTransfer"] = request.get_enable_offline_transfer()
        if request.get_offline_transfer_sound() is not None:
            body["offlineTransferSound"] = request.get_offline_transfer_sound()
        if request.get_password() is not None:
            body["password"] = request.get_password()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.CreateSubscribeRequest import CreateSubscribeRequest
        from gs2_chat_client.control.CreateSubscribeResult import CreateSubscribeResult
        return CreateSubscribeResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=CreateSubscribeRequest.Constant.MODULE,
            target_function=CreateSubscribeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_my_subscribe(self, request):
        """
        購読を解除する。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DeleteMySubscribeRequest.DeleteMySubscribeRequest
        """
        query_strings = {}
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DeleteMySubscribeRequest import DeleteMySubscribeRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/user/self/subscribe",
            service=self.ENDPOINT,
            component=DeleteMySubscribeRequest.Constant.MODULE,
            target_function=DeleteMySubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def delete_subscribe(self, request):
        """
        購読を解除する。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DeleteSubscribeRequest.DeleteSubscribeRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DeleteSubscribeRequest import DeleteSubscribeRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=DeleteSubscribeRequest.Constant.MODULE,
            target_function=DeleteSubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_my_subscribe(self, request):
        """
        ユーザが購読しているルームの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeMySubscribeRequest.DescribeMySubscribeRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeMySubscribeResult.DescribeMySubscribeResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeMySubscribeRequest import DescribeMySubscribeRequest

        from gs2_chat_client.control.DescribeMySubscribeResult import DescribeMySubscribeResult
        return DescribeMySubscribeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/user/subscribe",
            service=self.ENDPOINT,
            component=DescribeMySubscribeRequest.Constant.MODULE,
            target_function=DescribeMySubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_subscribe_by_room_id(self, request):
        """
        ルームを購読しているユーザの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeSubscribeByRoomIdRequest.DescribeSubscribeByRoomIdRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeSubscribeByRoomIdResult.DescribeSubscribeByRoomIdResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeSubscribeByRoomIdRequest import DescribeSubscribeByRoomIdRequest

        from gs2_chat_client.control.DescribeSubscribeByRoomIdResult import DescribeSubscribeByRoomIdResult
        return DescribeSubscribeByRoomIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=DescribeSubscribeByRoomIdRequest.Constant.MODULE,
            target_function=DescribeSubscribeByRoomIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_subscribe_by_user_id(self, request):
        """
        ユーザが購読しているルームの一覧を取得します。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.DescribeSubscribeByUserIdRequest.DescribeSubscribeByUserIdRequest
        :return: 結果
        :rtype: gs2_chat_client.control.DescribeSubscribeByUserIdResult.DescribeSubscribeByUserIdResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.DescribeSubscribeByUserIdRequest import DescribeSubscribeByUserIdRequest

        from gs2_chat_client.control.DescribeSubscribeByUserIdResult import DescribeSubscribeByUserIdResult
        return DescribeSubscribeByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=DescribeSubscribeByUserIdRequest.Constant.MODULE,
            target_function=DescribeSubscribeByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_my_subscribe(self, request):
        """
        購読情報を取得する。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.GetMySubscribeRequest.GetMySubscribeRequest
        :return: 結果
        :rtype: gs2_chat_client.control.GetMySubscribeResult.GetMySubscribeResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.GetMySubscribeRequest import GetMySubscribeRequest

        from gs2_chat_client.control.GetMySubscribeResult import GetMySubscribeResult
        return GetMySubscribeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/user/self/subscribe",
            service=self.ENDPOINT,
            component=GetMySubscribeRequest.Constant.MODULE,
            target_function=GetMySubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_subscribe(self, request):
        """
        購読情報を取得する。<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_chat_client.control.GetSubscribeRequest.GetSubscribeRequest
        :return: 結果
        :rtype: gs2_chat_client.control.GetSubscribeResult.GetSubscribeResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_chat_client.control.GetSubscribeRequest import GetSubscribeRequest

        from gs2_chat_client.control.GetSubscribeResult import GetSubscribeResult
        return GetSubscribeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/lobby/" + str(("null" if request.get_lobby_name() is None or request.get_lobby_name() == "" else url_encoder.encode(request.get_lobby_name()))) + "/room/" + str(("null" if request.get_room_id() is None or request.get_room_id() == "" else url_encoder.encode(request.get_room_id()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/subscribe",
            service=self.ENDPOINT,
            component=GetSubscribeRequest.Constant.MODULE,
            target_function=GetSubscribeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
