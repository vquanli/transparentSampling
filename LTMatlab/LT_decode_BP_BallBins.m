function [H_decode_after,code_decode_after,tag_decode] = LT_decode_BP_BallBins(H_receive,code_receive,H_decode_before,code_decode_before,packetnum,k_n)
    tag_decode = 0;
    H_decode_after = [H_decode_before;
                      H_receive];
    code_decode_after = [code_decode_before;
                        code_receive];
                    
    if size(find(H_receive == 1),2) == 1
        [H_decode_after,code_decode_after] = BP(H_decode_after,code_decode_after,size(H_decode_after,1));
        rank_H = find_rank(H_decode_after);
        % disp("2222222222222")
        % disp(rank_H)
        if rank_H >= (packetnum*k_n)
            % disp("111111111111111")
            % disp(packetnum)
            % disp(packetnum/k_n)
            % disp(rank_H)
            tag_decode = 1;
        end
    end

end
