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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_chat_client.Gs2Chat import Gs2Chat


class CheckEstimateScanByteByAllRoomRequest(Gs2BasicRequest):

    class Constant(Gs2Chat):
        FUNCTION = "CheckEstimateScanByteByAllRoom"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CheckEstimateScanByteByAllRoomRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__message = None
        else:
            self.set_message(params['message'] if 'message' in params.keys() else None)
        if params is None:
            self.__meta = None
        else:
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
        if params is None:
            self.__begin = None
        else:
            self.set_begin(params['begin'] if 'begin' in params.keys() else None)
        if params is None:
            self.__end = None
        else:
            self.set_end(params['end'] if 'end' in params.keys() else None)
        if params is None:
            self.__page_token = None
        else:
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
        if params is None:
            self.__limit = None
        else:
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

    def get_lobby_name(self):
        """
        ロビーの名前を取得
        :return: ロビーの名前
        :rtype: unicode
        """
        return self.__lobby_name

    def set_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        """
        if lobby_name and not (isinstance(lobby_name, str) or isinstance(lobby_name, unicode)):
            raise TypeError(type(lobby_name))
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_lobby_name(lobby_name)
        return self

    def get_user_id(self):
        """
        検索するユーザID文字列(部分一致)を取得
        :return: 検索するユーザID文字列(部分一致)
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        検索するユーザID文字列(部分一致)を設定
        :param user_id: 検索するユーザID文字列(部分一致)
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        検索するユーザID文字列(部分一致)を設定
        :param user_id: 検索するユーザID文字列(部分一致)
        :type user_id: unicode
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_user_id(user_id)
        return self

    def get_message(self):
        """
        検索するメッセージテキスト文字列(部分一致)を取得
        :return: 検索するメッセージテキスト文字列(部分一致)
        :rtype: unicode
        """
        return self.__message

    def set_message(self, message):
        """
        検索するメッセージテキスト文字列(部分一致)を設定
        :param message: 検索するメッセージテキスト文字列(部分一致)
        :type message: unicode
        """
        if message and not (isinstance(message, str) or isinstance(message, unicode)):
            raise TypeError(type(message))
        self.__message = message

    def with_message(self, message):
        """
        検索するメッセージテキスト文字列(部分一致)を設定
        :param message: 検索するメッセージテキスト文字列(部分一致)
        :type message: unicode
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_message(message)
        return self

    def get_meta(self):
        """
        検索するメッセージメタデータ文字列(部分一致)を取得
        :return: 検索するメッセージメタデータ文字列(部分一致)
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        検索するメッセージメタデータ文字列(部分一致)を設定
        :param meta: 検索するメッセージメタデータ文字列(部分一致)
        :type meta: unicode
        """
        if meta and not (isinstance(meta, str) or isinstance(meta, unicode)):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        検索するメッセージメタデータ文字列(部分一致)を設定
        :param meta: 検索するメッセージメタデータ文字列(部分一致)
        :type meta: unicode
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_meta(meta)
        return self

    def get_begin(self):
        """
        検索期間 開始日時（エポック秒）を取得
        :return: 検索期間 開始日時（エポック秒）
        :rtype: int
        """
        return self.__begin

    def set_begin(self, begin):
        """
        検索期間 開始日時（エポック秒）を設定
        :param begin: 検索期間 開始日時（エポック秒）
        :type begin: int
        """
        if begin and not isinstance(begin, int):
            raise TypeError(type(begin))
        self.__begin = begin

    def with_begin(self, begin):
        """
        検索期間 開始日時（エポック秒）を設定
        :param begin: 検索期間 開始日時（エポック秒）
        :type begin: int
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_begin(begin)
        return self

    def get_end(self):
        """
        検索期間 終了日時（エポック秒）を取得
        :return: 検索期間 終了日時（エポック秒）
        :rtype: int
        """
        return self.__end

    def set_end(self, end):
        """
        検索期間 終了日時（エポック秒）を設定
        :param end: 検索期間 終了日時（エポック秒）
        :type end: int
        """
        if end and not isinstance(end, int):
            raise TypeError(type(end))
        self.__end = end

    def with_end(self, end):
        """
        検索期間 終了日時（エポック秒）を設定
        :param end: 検索期間 終了日時（エポック秒）
        :type end: int
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_end(end)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        if page_token and not (isinstance(page_token, str) or isinstance(page_token, unicode)):
            raise TypeError(type(page_token))
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        if limit and not isinstance(limit, int):
            raise TypeError(type(limit))
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: CheckEstimateScanByteByAllRoomRequest
        """
        self.set_limit(limit)
        return self
