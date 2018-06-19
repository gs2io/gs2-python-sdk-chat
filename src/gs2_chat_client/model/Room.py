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


class Room(object):

    def __init__(self, params=None):
        if params is None:
            self.__room_id = None
            self.__allow_user_ids = None
            self.__need_password = None
            self.__create_at = None
        else:
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_allow_user_ids(params['allowUserIds'] if 'allowUserIds' in params.keys() else None)
            self.set_need_password(params['needPassword'] if 'needPassword' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)

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

    def get_allow_user_ids(self):
        """
        参加可能なユーザIDリストを取得
        :return: 参加可能なユーザIDリスト
        :rtype: list[unicode]
        """
        return self.__allow_user_ids

    def set_allow_user_ids(self, allow_user_ids):
        """
        参加可能なユーザIDリストを設定
        :param allow_user_ids: 参加可能なユーザIDリスト
        :type allow_user_ids: list[unicode]
        """
        self.__allow_user_ids = allow_user_ids

    def get_need_password(self):
        """
        メッセージの送受信にパスワードが必要かを取得
        :return: メッセージの送受信にパスワードが必要か
        :rtype: bool
        """
        return self.__need_password

    def set_need_password(self, need_password):
        """
        メッセージの送受信にパスワードが必要かを設定
        :param need_password: メッセージの送受信にパスワードが必要か
        :type need_password: bool
        """
        self.__need_password = need_password

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Room, self).__getitem__(key)

    def to_dict(self):
        return {
            "roomId": self.__room_id,
            "allowUserIds": self.__allow_user_ids,
            "needPassword": self.__need_password,
            "createAt": self.__create_at,
        }
