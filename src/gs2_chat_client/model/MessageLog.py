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


class MessageLog(object):

    def __init__(self, params=None):
        if params is None:
            self.__message_id = None
            self.__room_id = None
            self.__user_id = None
            self.__message = None
            self.__meta = None
            self.__create_at = None
        else:
            self.set_message_id(params['messageId'] if 'messageId' in params.keys() else None)
            self.set_room_id(params['roomId'] if 'roomId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_message(params['message'] if 'message' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)

    def get_message_id(self):
        """
        メッセージIDを取得
        :return: メッセージID
        :rtype: unicode
        """
        return self.__message_id

    def set_message_id(self, message_id):
        """
        メッセージIDを設定
        :param message_id: メッセージID
        :type message_id: unicode
        """
        self.__message_id = message_id

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

    def get_user_id(self):
        """
        発言者ユーザIDを取得
        :return: 発言者ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        発言者ユーザIDを設定
        :param user_id: 発言者ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_message(self):
        """
        メッセージテキストを取得
        :return: メッセージテキスト
        :rtype: unicode
        """
        return self.__message

    def set_message(self, message):
        """
        メッセージテキストを設定
        :param message: メッセージテキスト
        :type message: unicode
        """
        self.__message = message

    def get_meta(self):
        """
        メッセージメタデータを取得
        :return: メッセージメタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メッセージメタデータを設定
        :param meta: メッセージメタデータ
        :type meta: unicode
        """
        self.__meta = meta

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
        return super(MessageLog, self).__getitem__(key)

    def to_dict(self):
        return {
            "messageId": self.__message_id,
            "roomId": self.__room_id,
            "userId": self.__user_id,
            "message": self.__message,
            "meta": self.__meta,
            "createAt": self.__create_at,
        }
