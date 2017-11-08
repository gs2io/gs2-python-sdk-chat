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


class DescribeSubscribeByRoomIdRequest(Gs2BasicRequest):

    class Constant(Gs2Chat):
        FUNCTION = "DescribeSubscribeByRoomId"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeSubscribeByRoomIdRequest, self).__init__(params)
        if params is None:
            self.__lobby_name = None
            self.__room_id = None
            self.__page_token = None
            self.__limit = None
        else:
            self.set_lobby_name(params['lobbyName'] if 'lobbyName' in params.keys() else None)
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
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
        self.__lobby_name = lobby_name

    def with_lobby_name(self, lobby_name):
        """
        ロビーの名前を設定
        :param lobby_name: ロビーの名前
        :type lobby_name: unicode
        :return: this
        :rtype: DescribeSubscribeByRoomIdRequest
        """
        self.set_lobby_name(lobby_name)
        return self

    def get_room_id(self):
        """
        ルームIDを取得
        :return: ルームID
        :rtype: unicode
        """
        return self.__room_id

    def set_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        """
        self.__room_id = room_id

    def with_room_id(self, room_id):
        """
        ルームIDを設定
        :param room_id: ルームID
        :type room_id: unicode
        :return: this
        :rtype: DescribeSubscribeByRoomIdRequest
        """
        self.set_room_id(room_id)
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
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeSubscribeByRoomIdRequest
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
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeSubscribeByRoomIdRequest
        """
        self.set_limit(limit)
        return self
